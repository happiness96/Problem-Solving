# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline


def run():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    N, M = map(int, r_input().split())
    board = [list(r_input().rstrip()) for _ in range(N)]

    candidate = []

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'L':
                cnt = 0

                for k in range(4):
                    tmp_row = i + dx[k]
                    tmp_col = j + dy[k]

                    if 0 <= tmp_row < N and 0 <= tmp_col < M:
                        cnt += int(board[tmp_row][tmp_col] == 'L')

                if cnt == 1:
                    candidate.append([i, j])

    if not candidate:
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'L':
                    candidate.append([i, j])

    result = 0

    for can in candidate:
        visit = [[0] * M for _ in range(N)]
        visit[can[0]][can[1]] = 1

        queue = deque([[can[0], can[1]]])
        cnt = 0

        while True:
            for _ in range(len(queue)):
                loc = queue.popleft()

                for k in range(4):
                    tmp_row = loc[0] + dx[k]
                    tmp_col = loc[1] + dy[k]

                    if 0 <= tmp_row < N and 0 <= tmp_col < M:
                        if not visit[tmp_row][tmp_col] and board[tmp_row][tmp_col] == 'L':
                            queue.append([tmp_row, tmp_col])
                            visit[tmp_row][tmp_col] = 1

            if not queue:
                break
            cnt += 1

        if cnt > result:
            result = cnt

    print(result)


if __name__ == '__main__':
    run()

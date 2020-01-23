# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

if __name__ == '__main__':
    N = int(r_input())          # N: 공간의 크기

    baby_shark_size = 2         # 아기 상어의 크기
    baby_shark_loc = (0, 0)

    sharks_loc = {size: [] for size in range(1, 7)}

    board = [list(map(int, r_input().split())) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                baby_shark_loc = (i, j)
                board[i][j] = 0

            elif board[i][j]:
                sharks_loc[board[i][j]].append((i, j))

    result = 0
    eat_cnt = 0

    while True:
        can_eat = {}
        can_dist = 1

        queue = deque([baby_shark_loc])
        visit = [[0] * N for _ in range(N)]
        visit[baby_shark_loc[0]][baby_shark_loc[1]] = 1

        while queue:
            for _ in range(len(queue)):
                loc = queue.popleft()

                for k in range(4):
                    tmp_row = loc[0] + dx[k]
                    tmp_col = loc[1] + dy[k]

                    if 0 <= tmp_row < N and 0 <= tmp_col < N:
                        if not visit[tmp_row][tmp_col]:
                            if board[tmp_row][tmp_col] <= baby_shark_size:
                                visit[tmp_row][tmp_col] = 1
                                queue.append((tmp_row, tmp_col))

                                if 0 < board[tmp_row][tmp_col] < baby_shark_size:
                                    if tmp_row not in can_eat:
                                        can_eat[tmp_row] = {}

                                    can_eat[tmp_row][tmp_col] = board[tmp_row][tmp_col]

            if can_eat:
                break

            can_dist += 1

        if not can_eat:
            break

        row = min(can_eat)
        col = min(can_eat[row])
        size = can_eat[row][col]

        result += can_dist
        board[row][col] = 0

        sharks_loc[size].remove((row, col))

        baby_shark_loc = (row, col)

        eat_cnt += 1

        if eat_cnt == baby_shark_size:
            baby_shark_size += 1
            eat_cnt = 0

    print(result)

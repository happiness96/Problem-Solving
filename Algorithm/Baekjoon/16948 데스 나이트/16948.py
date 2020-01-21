# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

if __name__ == '__main__':
    N = int(r_input())
    r1, c1, r2, c2 = map(int, r_input().split())

    board = [[0] * N for _ in range(N)]

    board[r1][c1] = 1

    queue = deque([(r1, c1)])
    cnt = 0

    dx = [-2, -2, 0, 0, 2, 2]
    dy = [1, -1, 2, -2, 1, -1]

    while queue:
        for _ in range(len(queue)):
            loc = queue.popleft()

            if loc == (r2, c2):
                print(cnt)
                exit()

            for k in range(6):
                tmp_row = loc[0] + dx[k]
                tmp_col = loc[1] + dy[k]

                if 0 <= tmp_row < N and 0 <= tmp_col < N:
                    if not board[tmp_row][tmp_col]:
                        board[tmp_row][tmp_col] = 1
                        queue.append((tmp_row, tmp_col))

        cnt += 1

    print(-1)

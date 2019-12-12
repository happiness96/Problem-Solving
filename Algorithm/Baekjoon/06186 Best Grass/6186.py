# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

R, C = map(int, r_input().split())
farm = [list(r_input().rstrip()) for _ in range(R)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

cnt = 0

for i in range(R):
    for j in range(C):
        if farm[i][j] == '#':
            farm[i][j] = '.'

            stack = []
            stack.append([i, j])

            while stack:
                pos = stack.pop()

                for k in range(4):
                    tmp_row = pos[0] + dr[k]
                    tmp_col = pos[1] + dc[k]

                    if 0 <= tmp_row < R and 0 <= tmp_col < C:
                        if farm[tmp_row][tmp_col] == '#':
                            farm[tmp_row][tmp_col] = '.'
                            stack.append([tmp_row, tmp_col])

            cnt += 1

print(cnt)

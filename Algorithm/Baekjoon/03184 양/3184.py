# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

R, C = map(int, r_input().split())          # 필드의 크기
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

field = {}
visit = {i: [0]*C for i in range(R)}

cnt_sheep = 0
cnt_wolf = 0

for i in range(R):
    field[i] = list(r_input().rstrip())

    for j in range(C):
        if field[i][j] == '#':
            visit[i][j] = 1

for i in range(R):
    for j in range(C):
        if not visit[i][j]:
            stack = deque()
            stack.append([i, j])
            visit[i][j] = 1

            sheep = 0
            wolf = 0

            while stack:                # BFS
                loc = stack.popleft()
                row = loc[0]
                col = loc[1]

                if field[row][col] == 'o':
                    sheep += 1

                elif field[row][col] == 'v':
                    wolf += 1

                for k in range(4):
                    tmp_row = row + dr[k]
                    tmp_col = col + dc[k]

                    if 0 <= tmp_row < R and 0 <= tmp_col < C:
                        if not visit[tmp_row][tmp_col]:
                            visit[tmp_row][tmp_col] = 1
                            stack.append([tmp_row, tmp_col])

            if sheep > wolf:
                cnt_sheep += sheep

            else:
                cnt_wolf += wolf


print(cnt_sheep, cnt_wolf)

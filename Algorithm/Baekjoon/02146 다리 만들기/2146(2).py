# -*- encoding: utf-8 -*-
import sys
from collections import deque
from copy import deepcopy
r_input = sys.stdin.readline

# N: 지도의 크기
N = int(r_input())

board = [list(map(int, r_input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
queue_list = [[], []]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(row, col, value):
    visit[row][col] = 1
    board[row][col] = value

    queue = [(row, col)]
    tmp_list = []

    while queue:
        loc = queue.pop()
        flag = 0

        for k in range(4):
            tmp_row = loc[0] + dx[k]
            tmp_col = loc[1] + dy[k]

            if 0 <= tmp_row < N and 0 <= tmp_col < N:
                if not visit[tmp_row][tmp_col]:
                    if board[tmp_row][tmp_col] == 1:
                        visit[tmp_row][tmp_col] = 1
                        board[tmp_row][tmp_col] = value
                        queue.append((tmp_row, tmp_col))

                    elif board[tmp_row][tmp_col] == 0:
                        flag = 1

        if flag:
            tmp_list.append((loc[0], loc[1]))

    queue_list.append(tmp_list)


cnt = 2
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            bfs(i, j, cnt)
            cnt += 1

result = sys.maxsize

for i in range(2, cnt - 1):
    for j in range(i + 1, cnt):
        for a in queue_list[i]:
            for b in queue_list[j]:
                dist = abs(a[0] - b[0]) + abs(a[1] - b[1])

                if dist < result:
                    result = dist

print(result - 1)

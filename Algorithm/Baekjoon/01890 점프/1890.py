# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# N: 게임판의 크기
N = int(r_input())
board = [list(map(int, r_input().split())) for _ in range(N)]

queue = deque([[0, 0]])

# 목적지
dest = [N - 1, N - 1]
visit = [[0] * N for _ in range(N)]
dp = [[0] * N for _ in range(N)]

visit[queue[0][0]][queue[0][1]] = 1
dp[0][0] = 1

while queue:
    loc = queue.popleft()

    if loc != dest:
        tmp_row = loc[0] + board[loc[0]][loc[1]]
        tmp_col = loc[1] + board[loc[0]][loc[1]]

        if 0 <= tmp_row < N:
            if not visit[tmp_row][loc[1]]:
                visit[tmp_row][loc[1]] = 1
                queue.append([tmp_row, loc[1]])

        if 0 <= tmp_col < N:
            if not visit[loc[0]][tmp_col]:
                visit[loc[0]][tmp_col] = 1
                queue.append([loc[0], tmp_col])

for i in range(N):
    for j in range(i + 1):
        row = i - j
        col = j

        if visit[row][col]:
            tmp_row = row + board[row][col]
            tmp_col = col + board[row][col]

            if 0 <= tmp_row < N:
                dp[tmp_row][col] += dp[row][col]

            if 0 <= tmp_col < N:
                dp[row][tmp_col] += dp[row][col]

for i in range(N - 1):
    for j in range(N - 1 - i):
        row = N - 1 - j
        col = 1 + j + i

        if row == col == N - 1:
            break

        if visit[row][col]:
            tmp_row = row + board[row][col]
            tmp_col = col + board[row][col]

            if 0 <= tmp_row < N:
                dp[tmp_row][col] += dp[row][col]

            if 0 <= tmp_col < N:
                dp[row][tmp_col] += dp[row][col]

print(dp[-1][-1])

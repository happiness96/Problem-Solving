# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 게임 구역의 크기

board = {}
visit = {}

for i in range(N):
    board[i] = list(map(int, r_input().split()))
    visit[i] = [0] * N

stack = []

stack.append([0, 0])
visit[0][0] = 1

while stack:
    loc = stack.pop()

    row = loc[0] + board[loc[0]][loc[1]]
    col = loc[1] + board[loc[0]][loc[1]]

    if [N - 1, N - 1] in [[row, loc[1]], [loc[0], col]]:
        print('HaruHaru')
        exit()

    if row < N and board[row][loc[1]] != 0:
        if not visit[row][loc[1]]:
            stack.append([row, loc[1]])
            visit[row][loc[1]] = 1

    if col < N and board[loc[0]][col] != 0:
        if not visit[loc[0]][col]:
            stack.append([loc[0], col])
            visit[loc[0]][col] = 1

print('Hing')

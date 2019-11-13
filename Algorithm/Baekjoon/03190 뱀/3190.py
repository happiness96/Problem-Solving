# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

N = int(r_input())      # N: 보드의 크기
K = int(r_input())      # K: 사과의 개수

board = {0: [-1]*(N+2), N+1: [-1]*(N+2)}        # 보드

for i in range(1, N+1):
    board[i] = [-1] + [0]*N + [-1]

for i in range(K):
    row, col = map(int, r_input().split())
    board[row][col] = 1         # 사과가 있는 자리

L = int(r_input())      # 뱀의 방향 변환 횟수
direction = 0           # 방향 [오른쪽, 아래, 왼쪽, 위]
change = {}

for i in range(L):
    # X초 가 끝난 뒤 C 방향으로 90도 회전
    X, C = map(str, r_input().rstrip().split())
    change[int(X)] = C

snake = deque([[1, 1]])
sec = 0

while True:
    sec += 1
    x = snake[0][0]
    y = snake[0][1]

    if direction == 0:          # 오른쪽
        y += 1

    elif direction == 1:        # 아래
        x += 1

    elif direction == 2:        # 왼쪽
        y -= 1

    else:                       # 위
        x -= 1

    if board[x][y] == -1 or [x, y] in snake:            # 벽에 부딫히거나 자신의 몸과 부딫히면
        print(sec)
        break

    if board[x][y] != 1:                # 사과 칸이 아니라면
        snake.pop()

    if board[x][y] == 1:                # 사과를 먹었다면
        board[x][y] = 0

    snake.appendleft([x, y])
    
    if sec in change:           # 방향 전환
        if change[sec] == 'D':
            direction += 1

            if direction > 3:
                direction = 0

        else:
            direction -= 1

            if direction < 0:
                direction = 3

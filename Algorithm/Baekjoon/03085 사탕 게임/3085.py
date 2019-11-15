# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 보드의 크기
board = {}                  # 사탕이 채워져있는 보드
result = 0                  # 상근이가 먹을 수 있는 사탕 최대 개수

for i in range(N):
    board[i] = list(r_input().rstrip())


def check_up_down(r, c, color):     # 위 아래 사탕 체크
    global result

    popping = 0
    for i in range(r-1, -1, -1):
        if board[i][c] == color:
            popping += 1
        else:
            break

    for i in range(r+1, N):
        if board[i][c] == color:
            popping += 1
        else:
            break

    if popping > 0:
        popping += 1

    result = max(result, popping)


def check_left_right(r, c, color):          # 좌 우 사탕 체크
    global result

    popping = 0
    for j in range(c-1, -1, -1):
        if board[r][j] == color:
            popping += 1
        else:
            break

    for j in range(c+1, N):
        if board[r][j] == color:
            popping += 1
        else:
            break

    if popping > 0:
        popping += 1

    result = max(result, popping)


def change_right(row, col):         # 오른쪽 사탕과 바꾸는 함수
    board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]

    check_up_down(row, col, board[row][col])
    check_left_right(row, col, board[row][col])

    check_up_down(row, col + 1, board[row][col + 1])
    check_left_right(row, col + 1, board[row][col + 1])

    board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]


def change_down(row, col):          # 아래쪽 사탕과 바꾸는 함수
    board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]

    check_up_down(row, col, board[row][col])
    check_left_right(row, col, board[row][col])

    check_up_down(row + 1, col, board[row + 1][col])
    check_left_right(row + 1, col, board[row + 1][col])

    board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]


for i in range(N):
    for j in range(N):
        if j < N - 1:
            change_right(i, j)

        if i < N - 1:
            change_down(i, j)

print(result)

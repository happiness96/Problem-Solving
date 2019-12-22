# -*- encoding: utf-8 -*-
import sys
from copy import deepcopy
r_input = sys.stdin.readline

# 보드의 크기
N = int(r_input())
board = [list(map(int, r_input().split())) for _ in range(N)]


def move_left():            # 왼쪽으로 옮기기
    for i in range(N):
        tmp = 0
        tmp_ind = 0

        for j in range(N):
            if board[i][j]:
                if board[i][j] == tmp:
                    board[i][tmp_ind] = 2 * tmp
                    board[i][j] = 0
                    tmp = 0
                    tmp_ind = 0
                else:
                    tmp = board[i][j]
                    tmp_ind = j

    for i in range(N):
        tmp_list = []

        for j in range(N):
            if board[i][j]:
                tmp_list.append(board[i][j])

        board[i] = tmp_list + [0] * (N - len(tmp_list))


def move_right():           # 오른쪽으로 옮기기
    for i in range(N):
        tmp = 0
        tmp_ind = 0

        for j in range(N - 1, -1, -1):
            if board[i][j]:
                if board[i][j] == tmp:
                    board[i][tmp_ind] = 2 * tmp
                    board[i][j] = 0
                    tmp = 0
                    tmp_ind = 0
                else:
                    tmp = board[i][j]
                    tmp_ind = j

    for i in range(N):
        tmp_list = []

        for j in range(N):
            if board[i][j]:
                tmp_list.append(board[i][j])

        board[i] = [0] * (N - len(tmp_list)) + tmp_list


def move_up():              # 위로 옮기기
    for j in range(N):
        tmp = 0
        tmp_ind = 0

        for i in range(N):
            if board[i][j]:
                if board[i][j] == tmp:
                    board[tmp_ind][j] = 2 * tmp
                    board[i][j] = 0
                    tmp = 0
                    tmp_ind = 0
                else:
                    tmp = board[i][j]
                    tmp_ind = i

    for j in range(N):
        tmp_list = []
        for i in range(N):
            if board[i][j]:
                tmp_list.append(board[i][j])

        tmp_list += [0] * (N - len(tmp_list))

        for i in range(N):
            board[i][j] = tmp_list[i]


def move_down():            # 아래로 옮기기
    for j in range(N):
        tmp = 0
        tmp_ind = 0

        for i in range(N - 1, -1, -1):
            if board[i][j]:
                if board[i][j] == tmp:
                    board[tmp_ind][j] = 2 * tmp
                    board[i][j] = 0
                    tmp = 0
                    tmp_ind = 0
                else:
                    tmp = board[i][j]
                    tmp_ind = i

    for j in range(N):
        tmp_list = []
        for i in range(N):
            if board[i][j]:
                tmp_list.append(board[i][j])

        tmp_list = [0] * (N - len(tmp_list)) + tmp_list

        for i in range(N):
            board[i][j] = tmp_list[i]


def move(direction, cnt):        # 1: left, 2: right, 3: up, 4: down (dfs)
    global result, board
    copy_board = deepcopy(board)

    maximum = 0

    for i in range(N):
        maximum = max(maximum, max(board[i]))

    result = max(result, maximum)

    if cnt > 5:            # 5번 이내로 이동시킨 후
        return

    if direction == 1:
        move_left()

    elif direction == 2:
        move_right()

    elif direction == 3:
        move_up()

    else:
        move_down()

    if board == copy_board:         # 이동 시키나 마나 같다면 return
        return

    for i in range(1, 5):
        move(i, cnt + 1)

    board = copy_board


result = 0
for m in range(1, 5):
    move(m, 1)

print(result)

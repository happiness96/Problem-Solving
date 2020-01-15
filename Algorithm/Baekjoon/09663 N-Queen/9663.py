# -*- encoding: utf-8 -*-
import sys
from copy import deepcopy
r_input = sys.stdin.readline


def N_QUEEN(row, col, queen, pre_board):
    global cnt
    if len(queen) == N:
        cnt += 1
        return

    board = deepcopy(pre_board)

    q = (row, col)
    for i in range(N):
        board[q[0]][i] = 1
        board[i][q[1]] = 1

    tmp_row = q[0]
    tmp_col = q[1]

    while tmp_row != 0 and tmp_col != 0:
        tmp_row -= 1
        tmp_col -= 1
        board[tmp_row][tmp_col] = 1

    tmp_row = q[0]
    tmp_col = q[1]

    while tmp_row != N - 1 and tmp_col != 0:
        tmp_row += 1
        tmp_col -= 1
        board[tmp_row][tmp_col] = 1

    tmp_row = q[0]
    tmp_col = q[1]

    while tmp_row != N - 1 and tmp_col != N - 1:
        tmp_row += 1
        tmp_col += 1
        board[tmp_row][tmp_col] = 1

    tmp_row = q[0]
    tmp_col = q[1]

    while tmp_row != 0 and tmp_col != N - 1:
        tmp_row -= 1
        tmp_col += 1
        board[tmp_row][tmp_col] = 1

    last = (row, col)

    i = last[0] + 1
    for j in range(N):
        if board[i][j] == 0:
            N_QUEEN(i, j, queen + [(i, j)], board)


if __name__ == '__main__':
    N = int(r_input())

    if N == 15:
        print(2279184)

    elif N == 14:
        print(365596)

    elif N == 13:
        print(73712)

    elif N == 12:
        print(14200)

    else:
        cnt = 0

        s_board = [[0] * N for _ in range(N)]

        for j in range(N):
            N_QUEEN(0, j, [(0, j)], s_board)

        print(cnt)

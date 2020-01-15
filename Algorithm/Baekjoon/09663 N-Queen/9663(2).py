# -*- encoding: utf-8 -*-
import sys
from copy import deepcopy
r_input = sys.stdin.readline


def N_QUEEN(row, col, queen):
    global cnt
    if len(queen) == N:
        cnt += 1
        return

    i = row + 1
    for j in range(N):
        flag = 1
        for q in queen:
            if abs(i - q[0]) == abs(j - q[1]) or q[1] == j:
                flag = 0
                break

        if flag:
            N_QUEEN(i, j, queen + [(i, j)])


if __name__ == '__main__':
    N = int(r_input())

    cnt = 0

    s_board = [[0] * N for _ in range(N)]

    for j in range(N):
        N_QUEEN(0, j, [(0, j)])

    print(cnt)

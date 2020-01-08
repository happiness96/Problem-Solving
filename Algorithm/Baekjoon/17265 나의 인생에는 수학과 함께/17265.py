# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def calc(num1, oper, num2):
    if oper == '+':
        return num1 + num2

    elif oper == '-':
        return num1 - num2

    else:
        return num1 * num2


def dfs(row, col, value, op):
    global maximum, minimum
    visit[row][col] = 1

    if [row, col] == dest:
        maximum = max(maximum, value)
        minimum = min(minimum, value)
        visit[row][col] = 0
        return

    for k in range(2):
        tmp_row = row + dx[k]
        tmp_col = col + dy[k]

        if 0 <= tmp_row < N and 0 <= tmp_col < N:
            if not visit[tmp_row][tmp_col]:
                if op:
                    dfs(tmp_row, tmp_col, calc(value, op, int(board[tmp_row][tmp_col])), '')
                else:
                    dfs(tmp_row, tmp_col, value, board[tmp_row][tmp_col])

    visit[row][col] = 0


if __name__ == '__main__':
    N = int(r_input())      # 지도의 크기
    board = [list(map(str, r_input().rstrip().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]

    dx = [0, 1]
    dy = [1, 0]

    start = int(board[0][0])
    dest = [N - 1, N - 1]  # 목적지

    maximum = -sys.maxsize
    minimum = sys.maxsize

    dfs(0, 0, start, '')

    print(maximum, minimum)

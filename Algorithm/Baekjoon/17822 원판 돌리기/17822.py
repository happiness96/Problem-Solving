# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def searching(row, col):
    global flag

    for k in range(4):
        tmp_row = row - dx[k]
        tmp_col = col - dy[k]

        if 1 <= tmp_row <= N:
            if tmp_col == -1:
                tmp_col = M - 1

            elif tmp_col == M:
                tmp_col = 0

            if board[tmp_row][tmp_col] == val:
                flag = 1
                board[tmp_row][tmp_col] = 0

                searching(tmp_row, tmp_col)


if __name__ == '__main__':
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    N, M, T = map(int, r_input().split())

    board = [[]]

    for _ in range(N):
        board.append(list(map(int, r_input().split())))

    for _ in range(T):
        x, d, k = map(int, r_input().split())

        rot = N // x

        for mult in range(1, rot + 1):
            ind = x * mult

            if d == 0:
                board[ind] = board[ind][-k:] + board[ind][:-k]

            else:
                board[ind] = board[ind][k:] + board[ind][:k]

        g_flag = 0

        for i in range(1, N + 1):
            for j in range(M):
                if board[i][j]:
                    val = board[i][j]

                    flag = 0
                    searching(i, j)

                    if flag:
                        g_flag = 1
                        board[i][j] = 0

        if not g_flag:
            cnt = 0
            total = 0

            for i in range(1, N + 1):
                for v in board[i]:
                    if v:
                        cnt += 1
                        total += v

            if cnt:
                avg = total / cnt

                for i in range(1, N + 1):
                    for j in range(M):
                        if board[i][j] != 0:
                            if board[i][j] > avg:
                                board[i][j] -= 1

                            elif board[i][j] < avg:
                                board[i][j] += 1

    result = 0

    for i in range(1, N + 1):
        result += sum(board[i])

    print(result)

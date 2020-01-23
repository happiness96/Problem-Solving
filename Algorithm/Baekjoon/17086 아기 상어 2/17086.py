# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, r_input().split())

    sharks = []
    board = []

    for i in range(N):
        line = list(map(int, r_input().split()))
        board.append(line)

        for j in range(M):
            if line[j] == 1:
                sharks.append((i, j))

    result = 0

    for i in range(N):
        for j in range(M):
            if not board[i][j]:
                mini = 150
                for s in sharks:
                    di = min(abs(i - s[0]), abs(j - s[1]))

                    if i > s[0]:
                        tmp_i = i - di
                    else:
                        tmp_i = i + di

                    if j > s[1]:
                        tmp_j = j - di
                    else:
                        tmp_j = j + di

                    tmp = di + abs(tmp_i - s[0]) + abs(tmp_j - s[1])

                    if tmp < mini:
                        mini = tmp

                    if mini <= result:
                        break

                if mini > result:
                    result = mini

    print(result)

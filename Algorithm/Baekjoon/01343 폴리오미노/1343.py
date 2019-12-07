# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

board = r_input().rstrip()

result = ''
cnt = 0

length = len(board)

for i in range(length):
    if board[i] == 'X':
        cnt += 1

    if board[i] == '.' or i == length - 1:
        if cnt % 2:
            print(-1)
            exit()

        result += 'A' * (cnt // 4 * 4) + 'B' * (cnt % 4)

        if board[i] == '.':
            result += '.'

        cnt = 0

print(result)

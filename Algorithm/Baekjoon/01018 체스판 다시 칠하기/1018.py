# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())          # 체스판의 크기 (N x M)
chess = {}
result = 101800

for i in range(N):
    chess[i] = r_input().rstrip()


def check_board(row, col):          # 체스판 보드 칠하기
    global result
    cnt1 = 0
    cnt2 = 0

    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if chess[row + i][col + j] != 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if chess[row + i][col + j] != 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
            else:
                if j % 2 == 0:
                    if chess[row + i][col + j] != 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if chess[row + i][col + j] != 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
    result = min(result, min(cnt1, cnt2))


for i in range(N-7):
    for j in range(M-7):
        check_board(i, j)

print(result)

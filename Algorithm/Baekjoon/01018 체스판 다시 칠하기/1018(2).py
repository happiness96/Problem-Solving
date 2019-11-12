# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())          # 체스판의 크기 (N x M)
chess = {}
result = 101800

comp1 = 'WBWBWBWB'
comp2 = 'BWBWBWBW'

for i in range(N):
    chess[i] = r_input().rstrip()


def check_board(row, col):          # 체스판 보드 칠하기
    global result
    cnt1 = 0
    cnt2 = 0

    for i in range(8):
        temp = chess[row+i][col:col+8]
        if i % 2:
            for j in range(8):
                if comp1[j] != temp[j]:
                    cnt1 += 1
                if comp2[j] != temp[j]:
                    cnt2 += 1
        else:
            for j in range(8):
                if comp2[j] != temp[j]:
                    cnt1 += 1
                if comp1[j] != temp[j]:
                    cnt2 += 1

    result = min(result, min(cnt1, cnt2))


for i in range(N-7):
    for j in range(M-7):
        check_board(i, j)

print(result)

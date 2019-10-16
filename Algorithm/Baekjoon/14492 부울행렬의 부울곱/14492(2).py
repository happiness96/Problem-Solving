#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())            # N * N 행렬

A = {}
B = {}

for i in range(N):
    A[i] = list(map(int, r().split()))

for i in range(N):
    B[i] = list(map(int, r().split()))

cnt = 0             # 부울 곱 연산 후 1의 개수


def Cij(i,j):           # C_ij
    for k in range(N):
        if A[i][k] and B[k][j]:
            return 1
    return 0


for i in range(N):
    for j in range(N):
        cnt += Cij(i,j)
            
print(cnt)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())
A = [0] + list(map(int, r_input().split()))

for i in range(2, N + 1):
    A[i] += A[i - 1]

M = int(r_input())

for _ in range(M):
    i, j = map(int, r_input().split())
    print(A[j] - A[i - 1])

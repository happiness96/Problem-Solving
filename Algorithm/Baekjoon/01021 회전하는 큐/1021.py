# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())
A = list(range(1, N + 1))
result = 0

gap = 0

for m in map(int, r_input().split()):
    ind = A.index(m)
    cmp = N - gap - ind
    
    if ind <= cmp:
        result += ind

    else:
        result += cmp

    A = A[ind + 1:] + A[:ind]

    gap += 1

print(result)

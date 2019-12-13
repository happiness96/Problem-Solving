# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())

if N == 1:
    print(0)
    exit()

gap = 0

for i in range(2, N):
    if i % 2:
        gap += gap - 1
    else:
        gap += gap + 1

print(2 ** (N - 2) - gap)

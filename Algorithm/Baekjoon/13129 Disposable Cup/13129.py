# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

A, B, N = map(int, r().split())

for i in range(N):
    print(B + A * N + B * i, end=' ')

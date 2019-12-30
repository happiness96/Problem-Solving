# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())

for i in range(N):
    print(' ' * (N - i - 1) + '*' * (2 * i + 1))

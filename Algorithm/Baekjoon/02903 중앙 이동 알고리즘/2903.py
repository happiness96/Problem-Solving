# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())

dots = 2

for i in range(N):
    dots += dots - 1

print(dots ** 2)

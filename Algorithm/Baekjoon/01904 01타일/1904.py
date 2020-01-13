# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())

a = 1
b = 2

if N < 3:
    print(N)

else:
    for i in range(3, N + 1):
        a, b = b, (a + b) % 15746

    print(b)

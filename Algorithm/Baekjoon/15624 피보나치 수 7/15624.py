# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

n = int(r_input())
a, b = 0, 1

if n == 0:
    print(a)
    exit()

if n == 1:
    print(b)
    exit()

for i in range(1, n):
    a, b = b, a + b
    a %= 1000000007
    b %= 1000000007

print(b)

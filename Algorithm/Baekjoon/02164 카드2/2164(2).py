# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())
T = 0

if N == 1:
    print(1)
    exit()

while True:
    if N <= 2 ** T:
        T -= 1
        break
    T += 1

print(2 * (N - 2 ** T))

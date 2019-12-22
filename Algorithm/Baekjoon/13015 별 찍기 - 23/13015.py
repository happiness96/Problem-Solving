# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())

print('*' * N + ' ' * (2 * N - 3) + '*' * N)

for i in range(N - 2):
    print(' ' * (i + 1) + '*' + ' ' * (N - 2) + '*' + ' ' * (2 * (N - 2 - i) - 1) + '*' + ' ' * (N - 2) + '*')

print(' ' * (N - 1) + '*' + ' ' * (N - 2) + '*' + ' ' * (N - 2) + '*')

for i in range(N - 2):
    print(' ' * (N - i - 2) + '*' + ' ' * (N - 2) + '*' + ' ' * (2 * i + 1) + '*' + ' ' * (N - 2) + '*')

print('*' * N + ' ' * (2 * N - 3) + '*' * N)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, K = map(int, r_input().split())

save = list(range(1, N + 1))
index = -1

print('<', end='')
while save:
    index += K
    index %= N
    print(save.pop(index), end='')

    if save:
        print(', ', end='')

    index -= 1
    N -= 1

print('>')

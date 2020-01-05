# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())
numbers = [0] * (N + 1)

for num in map(int, r_input().split()):
    chk = num

    while chk <= N:
        numbers[chk] = chk
        chk += num

print(sum(numbers))

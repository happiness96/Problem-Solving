# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 선분의 개수

total = 0

a, b = map(int, r_input().split())
total += b - a

last = b

for i in range(N-1):
    x, y = map(int, r_input().split())

    if y > last:
        if x >= last:
            total += y - x
        else:
            total += y - last

        last = y

print(total)

# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

N = int(r())        # N: 트로피의 개수
trophy = [int(r()) for i in range(N)]

left_max = 0
left = 0

for t in trophy:
    if t > left_max:
        left += 1
        left_max = t

right_max = 0
right = 0

for t in trophy[::-1]:
    if t > right_max:
        right += 1
        right_max = t

print(left, right)

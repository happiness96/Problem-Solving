# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 타임머신 제한 시간
N = int(r_input())
coin = list(map(int, r_input().split()))

result = 0

tmp = coin.pop()

for c in coin[::-1]:
    if c < tmp:
        result += tmp - c
    else:
        tmp = c

print(result)

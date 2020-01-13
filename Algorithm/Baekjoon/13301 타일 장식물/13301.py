# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

dp = [4, 6]

for n in range(2, 81):
    dp.append(dp[-1] + dp[-2])

N = int(r_input())
print(dp[N - 1])

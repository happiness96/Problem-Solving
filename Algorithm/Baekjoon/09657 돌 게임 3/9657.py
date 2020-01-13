# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

dp = [0, 1, 0, 0]

for n in range(4, 1001):
    if dp[n - 1] or dp[n - 3] or dp[n - 4]:
        dp.append(0)
    else:
        dp.append(1)

N = int(r_input())
print('CY' if dp[N - 1] else 'SK')

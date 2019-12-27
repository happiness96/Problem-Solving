# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 집의 수
N = int(r_input())

dp = [0] * 3

for _ in range(N):
    r, g, b = map(int, r_input().split())

    dp[0], dp[1], dp[2] = min(dp[1], dp[2]) + r, min(dp[0], dp[2]) + g, min(dp[0], dp[1]) + b

print(min(dp))

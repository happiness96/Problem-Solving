# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

n = int(r_input())
wine = [int(r_input()) for _ in range(n)]

if n == 1:
    print(wine[0])
    exit()

dp = [[]] * n

dp[0] = [wine[0]]
dp[1] = [wine[1], wine[0] + wine[1]]

result = max(dp[0][0], max(dp[1]))

if n > 2:
    dp[2] = [max(dp[0]) + wine[2], dp[1][0] + wine[2]]

for i in range(3, n):
    if wine[i]:
        dp[i] = [max(max(dp[i - 2]), max(dp[i - 3])) + wine[i], dp[i - 1][0] + wine[i]]

        tmp = max(dp[i])
        if result < tmp:
            result = tmp

    else:
        tmp = max(max(dp[i - 2]), max(dp[i - 1]))
        dp[i] = [tmp, tmp]

print(result)

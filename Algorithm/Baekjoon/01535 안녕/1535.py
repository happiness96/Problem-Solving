# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 사람의 수
N = int(r_input())
# 각 사람에게 인사했을 때 잃는 체력
L = list(map(int, r_input().split()))
# 각 사람에게 인사했을 때 얻는 기쁨
J = list(map(int, r_input().split()))

dp = [0] * 101

for i in range(N):
    healthy = L[i]
    happiness = J[i]

    if healthy == 100:
        continue

    for j in range(healthy + 1, 101):
        if dp[j]:
            dp[j - healthy] = max(dp[j - healthy], dp[j] + happiness)

    dp[100 - healthy] = max(dp[100 - healthy], happiness)

print(max(dp))

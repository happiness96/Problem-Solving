# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    n, k = map(int, r_input().split())
    coin_list = []
    dp = [0] * (k + 1)

    for _ in range(n):
        cost = int(r_input())

        if cost <= k:
            coin_list.append(cost)

    for c in coin_list:
        dp[c] += 1

        for i in range(k):
            if dp[i]:
                value = i + c
                if value > k:
                    break
                else:
                    dp[value] += dp[i]

    print(dp[-1])


run()

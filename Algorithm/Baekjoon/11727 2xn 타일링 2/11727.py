# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


if __name__ == '__main__':
    N = int(r_input())

    dp = [1, 3, 5]

    for _ in range(N - 3):
        dp.append(dp[-1] + dp[-2] * 2)

    print(dp[N-1] % 10007)

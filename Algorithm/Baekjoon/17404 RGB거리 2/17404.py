# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

if __name__ == '__main__':
    N = int(r_input())
    first = list(map(int, r_input().split()))
    house = [list(map(int, r_input().split())) for _ in range(N - 1)]

    result = sys.maxsize

    for i in range(3):
        dp = [sys.maxsize] * 3
        dp[i] = first[i]

        for j in range(N - 1):
            r, g, b = house[j][0], house[j][1], house[j][2]

            r += min(dp[1], dp[2])
            g += min(dp[0], dp[2])
            b += min(dp[0], dp[1])

            dp = [r, g, b]

        tmp = sys.maxsize
        for k in range(3):
            if k != i:
                tmp = min(tmp, dp[k])

        result = min(result, tmp)

    print(result)

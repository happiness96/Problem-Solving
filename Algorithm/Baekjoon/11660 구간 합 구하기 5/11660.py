# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    N, M = map(int, r_input().split())

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        line = [0] + list(map(int, r_input().split()))

        for j in range(1, N + 1):
            if i == 0:
                if j == 0:
                    dp[i][j] = line[j]
                else:
                    dp[i][j] = dp[i][j - 1] + line[j]

            else:
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + line[j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + line[j]

    for _ in range(M):
        x1, y1, x2, y2 = map(int, r_input().split())

        print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])


if __name__ == '__main__':
    run()

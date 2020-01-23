# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    N = int(r_input())
    dp = [2, 6, 16]
    gap = [4, 10]

    if N < 3:
        print(dp[N - 1] + 1)
        exit()

    result = 16

    for _ in range(N - 3):
        gap[0], gap[1] = gap[1], (gap[1] * 2 + gap[0]) % 9901
        result += gap[1]

    print((result + 1) % 9901)


if __name__ == '__main__':
    run()

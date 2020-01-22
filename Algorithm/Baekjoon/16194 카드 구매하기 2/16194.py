# -*- encoding: utf-8 -*-
import sys
from copy import deepcopy
r_input = sys.stdin.readline


def run():
    N = int(r_input())

    cards = [0] + list(map(int, r_input().split()))
    dp = deepcopy(cards)

    for i in range(1, N // 2 + 1):
        for j in range(i, N + 1):
            ind = i + j

            if ind > N:
                break

            dp[ind] = min(dp[ind], dp[j] + cards[i])

    print(dp[-1])


if __name__ == '__main__':
    run()

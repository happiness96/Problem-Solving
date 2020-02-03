# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    L = int(r_input())
    N = int(r_input())

    roll_cake = [0] * (L + 1)

    max_cnt1 = 0
    max_cnt2 = 0
    result1 = 0
    result2 = 0

    for no in range(1, N + 1):
        P, K = map(int, r_input().split())

        cnt = 0

        for i in range(P, K + 1):
            if roll_cake[i] == 0:
                roll_cake[i] = no
                cnt += 1

        if cnt > max_cnt1:
            max_cnt1 = cnt
            result1 = no

        tmp = K - P + 1
        if tmp > max_cnt2:
            max_cnt2 = tmp
            result2 = no

    print(result2)
    print(result1)


if __name__ == '__main__':
    run()

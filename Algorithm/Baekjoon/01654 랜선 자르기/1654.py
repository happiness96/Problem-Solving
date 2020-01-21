# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def check(length):
    cnt = 0

    for line in lines_length:
        cnt += line // length

    return cnt >= N


if __name__ == '__main__':
    K, N = map(int, r_input().split())

    lines_length = [int(r_input()) for _ in range(K)]

    mini = 1
    maxi = sum(lines_length) // N

    while maxi - mini > 1:
        mid = (maxi + mini) // 2

        if check(mid):
            mini = mid

        else:
            maxi = mid

    if check(maxi):
        print(maxi)

    else:
        print(mini)

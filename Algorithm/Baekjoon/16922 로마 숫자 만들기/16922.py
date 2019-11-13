# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

nums = [1, 5, 10, 50]
N = int(r_input())          # 문자의 개수
result = []                 # 만들 수 있는 수


def how_many(ind, cnt, value):
    if ind == 3:
        value += (N - cnt) * nums[ind]

        if value not in result:
            result.append(value)

        return

    for i in range(N - cnt + 1):
        how_many(ind+1, cnt + i, value + nums[ind] * i)


how_many(0, 0, 0)
print(len(result))

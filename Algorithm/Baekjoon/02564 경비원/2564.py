# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

c, r = map(int, r_input().split())
# 상점의 개수
N = int(r_input())
locations = [list(map(int, r_input().split())) for _ in range(N)]
dong = list(map(int, r_input().split()))


def find_location(loc):
    if loc[0] == 1:
        return [r, loc[1]]

    elif loc[0] == 2:
        return [0, loc[1]]

    elif loc[0] == 3:
        return [r - loc[1], 0]

    else:
        return [r - loc[1], c]


dong_loc = find_location(dong)
result = 0

for i in range(N):
    store_loc = find_location(locations[i])

    tmp = [dong[0], locations[i][0]]
    if tmp in [[1, 2], [2, 1]]:
        result += min(dong_loc[1] + r + store_loc[1], c - dong_loc[1] + r + c - store_loc[1])

    elif tmp in [[3, 4], [4, 3]]:
        result += min(dong_loc[0] + c + store_loc[0], r - dong_loc[0] + c + r - store_loc[0])

    else:
        result += abs(dong_loc[0] - store_loc[0]) + abs(dong_loc[1] - store_loc[1])

print(result)

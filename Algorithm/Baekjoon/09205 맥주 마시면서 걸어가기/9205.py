# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def cal_distance(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


def floyd():
    for i in range(n + 2):
        for j in range(n + 2):
            for k in range(n + 2):
                if value[j][i] and value[i][k]:
                    value[j][k] = 1


# t: 테스트 케이스의 개수
t = int(r_input())

for _ in range(t):
    # n: 편의점의 개수
    n = int(r_input())

    # 상근이네 집
    my_house = list(map(int, r_input().split()))

    # 편의점
    store = [list(map(int, r_input().split())) for _ in range(n)]

    # 펜타포트 락 페스티벌
    festival = list(map(int, r_input().split()))

    value = [[0] * (n + 2) for _ in range(n + 2)]

    for i in range(n):
        for j in range(i + 1, n):
            dist = cal_distance(store[i], store[j])

            if dist <= 1000:
                value[i + 1][j + 1] = 1
                value[j + 1][i + 1] = 1

    for i in range(n):
        dist = cal_distance(my_house, store[i])

        if dist <= 1000:
            value[0][i + 1] = 1
            value[i + 1][0] = 1

    for i in range(n):
        dist = cal_distance(store[i], festival)

        if dist <= 1000:
            value[i + 1][n + 1] = 1
            value[n + 1][i + 1] = 1

    dist = cal_distance(my_house, festival)
    if dist <= 1000:
        value[0][n + 1] = 1
        value[n + 1][0] = 1

    floyd()

    print('happy' if value[0][-1] else 'sad')

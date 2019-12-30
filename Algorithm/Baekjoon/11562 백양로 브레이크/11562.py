# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# n: 건물의 수, m: 길의 수
n, m = map(int, r_input().split())
INF = sys.maxsize

building = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v, b = map(int, r_input().split())
    building[u][v] = 0
    building[v][u] = 1

    if b:
        building[v][u] = 0


def floyd():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                tmp = building[j][i] + building[i][k]
                if tmp < building[j][k]:
                    building[j][k] = tmp


floyd()

# k: 질문의 개수
k = int(r_input())

for _ in range(k):
    start, end = map(int, r_input().split())

    if start == end:
        print(0)
        continue

    print(building[start][end])

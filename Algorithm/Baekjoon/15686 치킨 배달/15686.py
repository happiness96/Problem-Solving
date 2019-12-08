# -*- encoding: utf-8 -*-
import sys
from itertools import combinations
r_input = sys.stdin.readline

# N x N 크기의 도시, M: 치킨집의 개수
N, M = map(int, r_input().split())

city = []
house = []
chicken = []        # 치킨집의 위치

INF = sys.maxsize

for i in range(N):
    city.append(list(map(int, r_input().split())))

    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

dist = [[0] * len(house) for _ in range(len(chicken))]

for i in range(len(chicken)):
    for j in range(len(house)):
        dist[i][j] = abs(chicken[i][0] - house[j][0]) + abs(chicken[i][1] - house[j][1])

result = INF

for locations in combinations(list(i for i in range(len(chicken))), M):
    total = 0

    for h in house:
        mini = INF
        for l in locations:
            tmp = abs(chicken[l][0] - h[0]) + abs(chicken[l][1] - h[1])

            if tmp < mini:
                mini = tmp

        total += mini

    if total < result:
        result = total

print(result)

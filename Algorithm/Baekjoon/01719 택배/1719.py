# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline

INF = sys.maxsize

# n: 집하장의 개수, m: 집하장간 경로의 개수
n, m = map(int, r_input().split())
cost = {}
result = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, r_input().split())

    if a not in cost:
        cost[a] = {}

    if b not in cost:
        cost[b] = {}

    if b not in cost[a]:
        cost[a][b] = c
        result[a][b] = b

    elif c < cost[a][b]:
        cost[a][b] = c
        result[a][b] = b

    if a not in cost[b]:
        cost[b][a] = c
        result[b][a] = a

    elif c < cost[b][a]:
        cost[b][a] = c
        result[b][a] = a


def dijkstra(node):
    if node not in cost:
        return

    queue = []
    value = [INF] * (n + 1)

    for v in cost[node]:
        value[v] = cost[node][v]
        heappush(queue, (value[v], v, v))

    while queue:
        mini = heappop(queue)
        min_value = mini[0]
        min_node = mini[1]
        parent = mini[2]

        if min_node in cost:
            for u in cost[min_node]:
                tmp = min_value + cost[min_node][u]

                if tmp < value[u]:
                    value[u] = tmp
                    result[node][u] = parent
                    heappush(queue, (tmp, u, parent))


for i in range(1, n + 1):
    dijkstra(i)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print('-' if i == j or result[i][j] == 0 else result[i][j], end=' ')
    print()

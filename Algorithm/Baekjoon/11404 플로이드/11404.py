# -*- encoding: utf-8 -*-
import sys
import heapq
r_input = sys.stdin.readline

n = int(r_input())          # 도시의 개수
m = int(r_input())          # 버스의 개수

bus = {}
cost = {}

for i in range(1, n + 1):
    bus[i] = {}
    cost[i] = ['INF'] * (n+1)
    cost[i][i] = 0

for i in range(m):
    # 도시 a에서 b로 이동하는 버스, 비용 c 소모
    a, b, c = map(int, r_input().split())

    if b in bus[a]:
        bus[a][b] = min(bus[a][b], c)
        cost[a][b] = min(cost[a][b], c)

    else:
        bus[a][b] = c
        cost[a][b] = c


def dijkstra(node, queue):
    while queue:
        mini = heapq.heappop(queue)
        min_cost = mini[0]
        min_node = mini[1]

        for N in bus[min_node]:
            tmp = min_cost + bus[min_node][N]

            if cost[node][N] == 'INF' or tmp < cost[node][N]:
                cost[node][N] = tmp
                heapq.heappush(queue, (tmp, N))


for i in range(1, n + 1):
    q = []

    for j in bus[i]:
        heapq.heappush(q, (bus[i][j], j))

    dijkstra(i, q)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if cost[i][j] == 'INF':
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()

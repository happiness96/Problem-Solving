# -*- encoding: utf-8 -*-
import sys
import heapq
r_input = sys.stdin.readline

# V: 정점의 개수, E: 간선의 개수
V, E = map(int, r_input().split())
start = int(r_input())          # 시작 정점

cost = {}

for i in range(E):
    u, v, w = map(int, r_input().split())

    if u not in cost:
        cost[u] = {}

    if v in cost[u]:
        cost[u][v] = min(cost[u][v], w)

    else:
        cost[u][v] = w

stack = ['INF'] * (V + 1)
stack[start] = 0
queue = []

for node in cost[start]:
    stack[node] = cost[start][node]
    heapq.heappush(queue, (cost[start][node], node))


def dijkstra():
    while queue:
        mini = heapq.heappop(queue)
        min_cost = mini[0]
        min_node = mini[1]

        if min_node in cost:
            for n in cost[min_node]:
                tmp = min_cost + cost[min_node][n]

                if stack[n] == 'INF' or tmp < stack[n]:
                    heapq.heappush(queue, (tmp, n))
                    stack[n] = tmp


dijkstra()

for i in range(1, V + 1):
    print(stack[i])

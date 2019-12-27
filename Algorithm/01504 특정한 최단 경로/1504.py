# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline

N, E = map(int, r_input().split())

graph = {}

for _ in range(E):
    a, b, c = map(int, r_input().split())

    if a not in graph:
        graph[a] = {}

    if b not in graph:
        graph[b] = {}

    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)

    else:
        graph[a][b] = c

    if a in graph[b]:
        graph[b][a] = min(graph[b][a], c)

    else:
        graph[b][a] = c


v1, v2 = map(int, r_input().split())


def dijkstra(start, end):
    INF = sys.maxsize
    stack = [INF] * (N + 1)
    stack[start] = 0

    queue = []

    if start in graph:
        for node in graph[start]:
            heappush(queue, (graph[start][node], node))
            stack[node] = graph[start][node]

    while queue:
        mini = heappop(queue)
        min_cost = mini[0]
        min_node = mini[1]

        if min_node in graph:
            for node in graph[min_node]:
                tmp = min_cost + graph[min_node][node]
                if tmp < stack[node]:
                    stack[node] = tmp
                    heappush(queue, (tmp, node))

    if stack[end] == INF:
        return -1

    else:
        return stack[end]


t1 = dijkstra(1, v1)
if t1 >= 0:
    t2 = dijkstra(v1, v2)
    if t2 >= 0:
        t3 = dijkstra(v2, N)
        if t3 >= 0:
            cost1 = t1 + t2 + t3
        else:
            cost1 = -1
    else:
        cost1 = -1
else:
    cost1 = -1

t4 = dijkstra(1, v2)
if t4 >= 0:
    t5 = dijkstra(v2, v1)
    if t5 >= 0:
        t6 = dijkstra(v1, N)
        if t6 >= 0:
            cost2 = t4 + t5 + t6
        else:
            cost2 = -1
    else:
        cost2 = -1
else:
    cost2 = -1

if cost1 < 0 and cost2 < 0:
    print(-1)

elif cost1 < 0:
    print(cost2)

elif cost2 < 0:
    print(cost1)

else:
    print(min(cost1, cost2))

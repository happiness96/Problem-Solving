# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline


def dijkstra(node):
    INF = sys.maxsize

    dijkstra_list = [INF] * (N + 1)

    queue = []
    visit = [0] * (N + 1)
    visit[node] = 1

    for n in dist[node]:
        dijkstra_list[n] = 1
        heappush(queue, (1, n))
        visit[n] = 1

    while queue:
        pop_value = heappop(queue)
        v = pop_value[0]
        v_n = pop_value[1]

        for n in dist[v_n]:
            if not visit[n]:
                tmp = v + 1

                if tmp < dijkstra_list[n]:
                    dijkstra_list[n] = tmp
                    heappush(queue, (tmp, n))

                visit[n] = 1

    max_value = max(dijkstra_list[2:])
    print(dijkstra_list.index(max_value), max_value, dijkstra_list.count(max_value))


if __name__ == '__main__':
    # N: 헛간의 개수, M: 길의 수
    N, M = map(int, r_input().split())

    dist = {node: [] for node in range(1, N + 1)}

    for _ in range(M):
        a, b = map(int, r_input().split())
        dist[a].append(b)
        dist[b].append(a)

    dijkstra(1)

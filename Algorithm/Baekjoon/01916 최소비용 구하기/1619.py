# -*- encoding: utf-8 -*-
import sys
import heapq
r_input = sys.stdin.readline

N = int(r_input())          # 도시의 개수
M = int(r_input())          # 버스의 개수

bus = {}

for i in range(1, N+1):
    bus[i] = {}

for i in range(M):
    a, b, c = map(int, r_input().split())

    if b in bus[a]:
        bus[a][b] = min(bus[a][b], c)

    else:
        bus[a][b] = c

a, b = map(int, r_input().split())

stack = ['INF'] * (N + 1)
stack[a] = 0

parents_node = [0] * (N + 1)            # 각 노드의 최소 비용 부모 노드

queue = []

for node in bus[a]:
    stack[node] = bus[a][node]
    parents_node[node] = a

    heapq.heappush(queue, (bus[a][node], node))

while queue:
    mini = heapq.heappop(queue)
    minimum = mini[0]
    min_node = mini[1]

    for n in bus[min_node]:
        tmp = minimum + bus[min_node][n]

        if stack[n] == 'INF' or tmp < stack[n]:
            stack[n] = tmp
            parents_node[n] = min_node

            heapq.heappush(queue, (tmp, n))

print(stack[b])

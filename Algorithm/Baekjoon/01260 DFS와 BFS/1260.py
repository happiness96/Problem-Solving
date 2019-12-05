import sys
from heapq import *
from collections import deque
from copy import deepcopy
r_input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# N: 정점의 개수, M: 간선의 개수, V: 시작 정점
N, M, V = map(int, r_input().split())

connect = [[] for _ in range(1001)]

for _ in range(M):
    a, b = map(int, r_input().split())
    connect[a].append(b)
    connect[b].append(a)


def dfs(node):
    print(node, end=' ')
    visit[node] = 1

    queue = deepcopy(connect[node])
    heapify(queue)

    while queue:
        num = heappop(queue)
        if not visit[num]:
            dfs(num)


def bfs(node):
    queue = deque()
    queue.append(node)
    visit[node] = 1

    while queue:
        num = queue.popleft()
        print(num, end=' ')

        hq = connect[num]
        heapify(hq)

        while hq:
            n = heappop(hq)
            if not visit[n]:
                visit[n] = 1
                queue.append(n)


visit = [0] * 1001
dfs(V)

print()

visit = [0] * 1001
bfs(V)

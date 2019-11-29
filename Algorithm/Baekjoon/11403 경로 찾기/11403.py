# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 정점의 개수
graph = {}

line = {}               # 간선

for i in range(N):
    graph[i] = list(map(int, r_input().split()))
    line[i] = set()

    for j in range(N):
        if graph[i][j]:
            line[i].add(j)


def find_path(node):
    go = 1
    for c in list(line[node]):
        sub = line[c] - line[node]
        line[node].update(sub)

        for i in sub:
            graph[node][i] = 1

        if sub:
            go = 0

    return go


while True:
    is_end = []
    for i in range(N):
        is_end.append(find_path(i))

    if is_end == [1] * N:
        break


for i in range(N):
    for j in range(N):
        print(graph[i][j], end=' ')
    print()

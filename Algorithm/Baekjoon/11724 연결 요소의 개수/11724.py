# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, r_input().split())      # N: 정점의 개수, M: 간선의 개수

cnt = 0

line = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, r_input().split())

    line[u].append(v)
    line[v].append(u)


def remove_line(node):
    for w in line.pop(node):
        if w in line:
            remove_line(w)


for i in range(1, N + 1):
    if i in line:
        remove_line(i)
        cnt += 1

print(cnt)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 도시의 수
N = int(r_input())
cost = [list(map(int, r_input().split())) for _ in range(N)]
result = sys.maxsize
visit = [0] * N


def dfs(node, total, cnt, start, p):
    global result
    visit[node] = 1

    if cnt == N:
        if cost[node][start]:
            total += cost[node][start]

            if total < result:
                result = total

        visit[node] = 0

        return

    for j in range(N):
        if j != start and not visit[j] and cost[node][j]:
            dfs(j, total + cost[node][j], cnt + 1, start, p + [j])

    visit[node] = 0


dfs(0, 0, 1, 0, [0])

print(result)

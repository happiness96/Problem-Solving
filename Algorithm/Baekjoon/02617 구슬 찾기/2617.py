# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def dfs(node, weight_list):
    global visit_list

    for t in weight_list[node]:
        if not visit_list[t]:
            visit_list[t] = 1
            dfs(t, weight_list)


if __name__ == '__main__':
    N, M = map(int, r_input().split())

    heavier = [[] for _ in range(N + 1)]
    lighter = [[] for _ in range(N + 1)]

    center = N // 2

    for _ in range(M):
        a, b = map(int, r_input().split())
        lighter[a].append(b)
        heavier[b].append(a)

    result = [0] * (N + 1)

    for i in range(1, N + 1):
        visit_list = [0] * (N + 1)
        dfs(i, heavier)
    
        if visit_list.count(1) > center:
            result[i] = 1

    for i in range(1, N + 1):
        visit_list = [0] * (N + 1)
        dfs(i, lighter)

        if visit_list.count(1) > center:
            result[i] = 1

    print(result.count(1))

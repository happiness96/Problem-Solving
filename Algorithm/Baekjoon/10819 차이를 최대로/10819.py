# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def dfs(node, total, depth):
    global result

    if depth == N:
        if total > result:
            result = total
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            dfs(i, total + abs(A[node] - A[i]), depth + 1)
            visit[i] = 0


if __name__ == '__main__':
    N = int(r_input())
    A = list(map(int, r_input().split()))

    visit = [0] * N

    result = 0

    for i in range(N):
        visit[i] = 1
        dfs(i, 0, 1)
        visit[i] = 0

    print(result)

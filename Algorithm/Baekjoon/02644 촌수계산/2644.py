# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline


def run():
    n = int(r_input())
    a, b = map(int, r_input().split())

    m = int(r_input())

    parent = [0] * (n + 1)
    child = {num: [] for num in range(1, n + 1)}

    for _ in range(m):
        x, y = map(int, r_input().split())
        child[x].append(y)
        parent[y] = x

    queue = deque([a])

    visit = [0] * (n + 1)
    visit[a] = 1

    result = 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            if node == b:
                print(result)
                exit()

            if parent[node]:
                if not visit[parent[node]]:
                    visit[parent[node]] = 1
                    queue.append(parent[node])

            for ch in child[node]:
                if not visit[ch]:
                    visit[ch] = 1
                    queue.append(ch)

        result += 1
        
    print(-1)


if __name__ == '__main__':
    run()

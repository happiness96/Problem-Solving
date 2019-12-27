# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

test_case = 1


def find_tree():            # 트리를 찾는 함수
    cnt = 0  # 트리의 개수

    for i in range(1, n + 1):
        if not visit[i]:
            queue = deque([(i, i)])
            visit[i] = 1

            flag = 1

            while queue:
                tmp = queue.popleft()
                parent = tmp[1]

                for node in graph[tmp[0]]:
                    if node != parent:
                        if visit[node]:
                            flag = 0

                        else:
                            queue.append((node, tmp[0]))
                            visit[node] = 1

            cnt += flag

    return cnt


while True:
    # n: 정점의 개수, m: 간선의 개수
    n, m = map(int, r_input().split())

    if n == m == 0:
        break

    graph = {num: [] for num in range(1, n + 1)}
    visit = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, r_input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = find_tree()

    print('Case ' + str(test_case) + ': ', end='')

    if not result:
        print('No trees.')

    elif result == 1:
        print('There is one tree.')

    else:
        print('A forest of ' + str(result) + ' trees.')

    test_case += 1

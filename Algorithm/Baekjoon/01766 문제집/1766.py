# -*- encoding: utf-8 -*-
import sys
import heapq
r_input = sys.stdin.readline

# N: 문제의 수, M: 먼저 푸는 것이 좋은 문제에 대한 정보의 수
N, M = map(int, r_input().split())
info1 = [0] * (N+1)                  # 각 문제보다 먼저 풀어야 할 문제 개수 (간선의 개수)
info2 = {}                       # 각 문제 이후에 풀어야 할 문제 리스트 {n: [n 이후에 풀어야 할 문제 목록]}

temp = {}

for i in range(M):
    A, B = map(int, r_input().split())          # A보다 B를 먼저 푸는 것이 좋다.

    info1[B] += 1

    if A in info2:
        info2[A].append(B)

    else:
        info2[A] = [B]

queue = []
stack = []

for i in range(1, N+1):             # 위상 정렬
    if not info1[i]:
        heapq.heappush(queue, i)

while queue:
    temp1 = heapq.heappop(queue)
    stack.append(str(temp1))

    if temp1 in info2:
        for t in info2[temp1]:
            info1[t] -= 1

            if not info1[t]:
                heapq.heappush(queue, t)

print(' '.join(stack))

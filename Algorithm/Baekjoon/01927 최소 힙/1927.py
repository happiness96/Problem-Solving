# -*- encoding: utf-8 -*-
import sys
import heapq
r_input = sys.stdin.readline

N = int(r_input())          # 연산의 개수
heap = []                   # 최소 힙 생성

for i in range(N):
    x = int(r_input())          # 연산 x

    if x:
        heapq.heappush(heap, x)

    else:
        if heap:
            print(heapq.heappop(heap))

        else:
            print(0)

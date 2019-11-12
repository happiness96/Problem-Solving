# -*- encoding: utf-8 -*-
import sys
import heapq
r_input = sys.stdin.readline

N = int(r_input())          # 로프의 개수
rope = []                   # 각 로프가 버틸 수 있는 최대 중량
result = 0                  # 최대 중량

for i in range(N):
    heapq.heappush(rope, int(r_input()))

for i in range(N):
    temp = heapq.heappop(rope)
    result = max(result, temp * (N - i))

print(result)

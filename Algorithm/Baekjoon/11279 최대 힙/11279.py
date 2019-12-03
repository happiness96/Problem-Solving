import sys
import heapq
r_input = sys.stdin.readline

N = int(r_input())      # N: 연산의 개수
queue = []

for i in range(N):
    x = int(r_input())

    if x:
        heapq.heappush(queue, -x)
    else:
        print(-heapq.heappop(queue) if queue else 0)

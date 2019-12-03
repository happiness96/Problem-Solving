import sys
import heapq
r_input = sys.stdin.readline

N = int(r_input())      # N: 연산의 개수
queue = []

for i in range(N):
    x = int(r_input())

    if x == 0:
        print(heapq.heappop(queue)[1] if queue else 0)

    else:
        heapq.heappush(queue, (abs(x), x))

import sys
import heapq
r_input = sys.stdin.readline

N = int(r_input())      # N: 카드 묶음의 개수
queue = [int(r_input()) for _ in range(N)]

heapq.heapify(queue)
total = 0

while True:
    num1 = heapq.heappop(queue)

    if not queue:
        break

    num2 = heapq.heappop(queue)

    plus = num1 + num2
    total += plus

    heapq.heappush(queue, plus)

print(total)

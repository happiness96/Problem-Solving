import sys
from heapq import *
r_input = sys.stdin.readline

N = int(r_input())      # 수빈이가 외치는 정수의 개수

left_size = 0
right_size = 0

left_queue = []
right_queue = []

for _ in range(N):
    num = int(r_input())

    if left_size and -left_queue[0] > num:
        heappush(right_queue, -heapreplace(left_queue, -num))

    else:
        heappush(right_queue, num)

    right_size += 1

    if right_size - left_size == 2:
        heappush(left_queue, -heappop(right_queue))
        left_size += 1
        right_size -= 1

    print(-left_queue[0] if left_size == right_size else right_queue[0])

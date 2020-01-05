# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# 명령의 수
N = int(r_input())
queue = deque()

for _ in range(N):
    order = r_input().rstrip()

    if order == 'size':
        print(len(queue))

    elif order == 'empty':
        print(0 if queue else 1)

    elif order == 'front':
        print(queue[0] if queue else -1)

    elif order == 'back':
        print(queue[-1] if queue else -1)

    elif order == 'pop':
        print(queue.popleft() if queue else -1)

    else:
        X = int(order[5:])
        queue.append(X)

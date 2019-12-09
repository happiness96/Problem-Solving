# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline

N = int(r_input())
queue = list(map(int, r_input().split()))

heapify(queue)

for _ in range(N - 1):
    for num in map(int, r_input().split()):
        if num > queue[0]:
            heapreplace(queue, num)

print(queue[0])

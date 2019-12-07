# -*- encoding: utf-8 -*-
import sys
import heapq
r_input = sys.stdin.readline

while True:
    N, M = map(int, r_input().split())

    if not N:
        break

    score = {}

    for _ in range(N):
        for num in map(int, r_input().split()):
            if num in score:
                score[num] += 1
            else:
                score[num] = 1

    queue = []
    for s in score:
        heapq.heappush(queue, (-score[s], s))

    first_score = -heapq.heappop(queue)[0]

    while True:
        tmp = heapq.heappop(queue)
        if -tmp[0] != first_score:
            second_score = -tmp[0]
            print(tmp[1], end=' ')
            break

    while queue:
        tmp = heapq.heappop(queue)
        if -tmp[0] == second_score:
            print(tmp[1], end=' ')
        else:
            break
    print()

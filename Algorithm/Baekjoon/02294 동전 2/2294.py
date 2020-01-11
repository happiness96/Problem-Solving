# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline


def run():
    n, k = map(int, r_input().split())
    coin_list = []
    visit = [0] * k
    queue = deque()

    for _ in range(n):
        cost = int(r_input())

        if cost == k:
            print(1)
            exit()

        if cost < k:
            if cost not in coin_list:
                coin_list.append(cost)
                queue.append(cost)
                visit[cost] = 1

    cnt = 2
    while queue:
        for _ in range(len(queue)):
            value = queue.popleft()

            for v in coin_list:
                tmp = value + v

                if tmp == k:
                    print(cnt)
                    exit()

                if tmp < k and not visit[tmp]:
                    queue.append(tmp)
                    visit[tmp] = 1

        cnt += 1

    print(-1)


run()

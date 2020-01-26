# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline


def run():
    n = int(r_input())

    queue = deque([0])
    cnt = 1
    visit = [0] * (n + 1)

    while True:
        for _ in range(len(queue)):
            node = queue.popleft()

            for i in range(1, n):
                val = node + i ** 2

                if val > n:
                    break

                if val == n:
                    print(cnt)
                    exit()

                if not visit[val]:
                    queue.append(val)
                    visit[val] = 1
        cnt += 1


if __name__ == '__main__':
    run()

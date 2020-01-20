# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

if __name__ == '__main__':
    F, S, G, U, D = map(int, r_input().split())

    visit = [0] * (F + 1)

    queue = deque([S])
    visit[S] = 1
    cnt = 0

    while queue:
        for _ in range(len(queue)):
            floor = queue.popleft()

            if floor == G:
                print(cnt)
                exit()

            up = floor + U
            down = floor - D

            if up <= F:
                if not visit[up]:
                    queue.append(up)
                    visit[up] = 1

            if down > 0:
                if not visit[down]:
                    queue.append(down)
                    visit[down] = 1

        cnt += 1

    print('use the stairs')

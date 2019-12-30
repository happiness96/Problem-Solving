# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline


def run():
    # N: 수빈이의 현재 위치, K: 동생의 현재 위치
    N, K = map(int, r_input().split())

    cnt = 0
    queue = deque([N])
    visit = [0] * (max(N, K) * 2 + 1)

    visit[N] = 1

    while True:
        flag = 0

        for _ in range(len(queue)):
            tmp = queue.popleft()

            if tmp == K:
                flag = 1
                break

            if K > tmp:
                a = 2 * tmp
                if not visit[a]:
                    queue.append(a)
                    visit[a] = 1

            b = min(tmp + 1, max(N, K) * 2)
            if not visit[b]:
                queue.append(b)
                visit[b] = 1

            c = max(tmp - 1, 0)
            if not visit[c]:
                queue.append(c)
                visit[c] = 1

        if flag:
            break

        cnt += 1

    print(cnt)


run()

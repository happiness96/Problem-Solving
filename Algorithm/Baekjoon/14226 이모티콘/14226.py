# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline


def run():
    queue = deque([(1, 0, 0)])
    S = int(r_input())

    visit = [[0] * (S + 1) for _ in range(S + 1)]

    time = 0

    while True:
        for _ in range(len(queue)):
            cnt = queue.popleft()

            if cnt[0] == S:
                print(time)
                sys.exit()

            if cnt[2] == 0:
                queue.append((cnt[0], cnt[0], 1))

            if cnt[1]:
                tmp = cnt[0] + cnt[1]
                if tmp < S + 1:
                    if not visit[tmp][cnt[1]]:
                        visit[tmp][cnt[1]] = 1
                        queue.append((tmp, cnt[1], 0))

            tmp = cnt[0] - 1
            if tmp > 1:
                if not visit[tmp][cnt[1]]:
                    visit[tmp][cnt[1]] = 1
                    queue.append((tmp, cnt[1], 0))

        time += 1


if __name__ == '__main__':
    run()

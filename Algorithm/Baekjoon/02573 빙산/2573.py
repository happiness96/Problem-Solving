# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def run():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 행의 개수, 열의 개수
    N, M = map(int, r_input().split())

    # 빙산의 높이
    queue = deque()
    iceberg = [list(map(int, r_input().split()))]
    chk = [[0] * M for _ in range(N)]

    for i in range(1, N - 1):
        height = list(map(int, r_input().split()))

        for j in range(1, M - 1):
            v = height[j]

            if v:
                chk[i][j] = 1
                queue.append((i, j, v))

        iceberg.append(height)

    iceberg.append(list(map(int, r_input().split())))

    year = 0

    while True:
        if queue:
            sub_queue = deque()
            sub_queue.append(queue[0])

            chk[queue[0][0]][queue[0][1]] = 0

            while sub_queue:
                tmp_loc = sub_queue.popleft()

                for k in range(4):
                    tmp_row = tmp_loc[0] + dx[k]
                    tmp_col = tmp_loc[1] + dy[k]

                    if chk[tmp_row][tmp_col]:
                        chk[tmp_row][tmp_col] = 0
                        sub_queue.append((tmp_row, tmp_col))

            for i in range(N):
                for j in range(M):
                    if chk[i][j]:
                        print(year)
                        exit()

        change = []

        for i in range(len(queue)):
            loc = queue.popleft()
            cnt = 0

            chk[loc[0]][loc[1]] = 1

            for k in range(4):
                if not iceberg[loc[0] + dx[k]][loc[1] + dy[k]]:
                    cnt += 1

            if cnt >= loc[2]:
                change.append((loc[0], loc[1], 0))
                chk[loc[0]][loc[1]] = 0

            else:
                tmp = loc[2] - cnt
                change.append((loc[0], loc[1], tmp))
                queue.append((loc[0], loc[1], tmp))

        for l in change:
            iceberg[l[0]][l[1]] = l[2]

        if not queue:
            print(0)
            break

        year += 1


run()

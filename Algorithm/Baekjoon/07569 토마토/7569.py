# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline


def run():
    M, N, H = map(int, r_input().split())

    tomatoes_queue = deque()
    tomatoes = []

    for i in range(H):
        tomatoes.append([])

        for j in range(N):
            tomatoes_list = list(map(int, r_input().split()))

            for k in range(M):
                if tomatoes_list[k] == 1:
                    tomatoes_queue.append((i, j, k))

            tomatoes[i].append(tomatoes_list)

    dx = [0, 0, 1, -1, 0, 0]
    dy = [1, -1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    cnt = 0

    while tomatoes_queue:
        for _ in range(len(tomatoes_queue)):
            loc = tomatoes_queue.popleft()

            for k in range(6):
                tmp_x = loc[0] + dx[k]
                tmp_y = loc[1] + dy[k]
                tmp_z = loc[2] + dz[k]

                if 0 <= tmp_x < H and 0 <= tmp_y < N and 0 <= tmp_z < M:
                    if tomatoes[tmp_x][tmp_y][tmp_z] == 0:
                        tomatoes[tmp_x][tmp_y][tmp_z] = 1
                        tomatoes_queue.append((tmp_x, tmp_y, tmp_z))

        if tomatoes_queue:
            cnt += 1

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoes[i][j][k] == 0:
                    print(-1)
                    exit()

    print(cnt)


if __name__ == '__main__':
    run()

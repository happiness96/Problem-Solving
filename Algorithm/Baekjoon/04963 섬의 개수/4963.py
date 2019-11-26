# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

dx = [0, 1, -1, 0, 1, 1, -1, -1]
dy = [1, 0, 0, -1, -1, 1, 1, -1]

while True:
    w, h = map(int, r_input().split())          # 섬의 너비 w와 높이 h

    if w == h == 0:
        break

    island = {}             # 지도

    cnt = 0                 # 섬의 개수

    for i in range(h):
        island[i] = list(map(int, r_input().split()))

    # BFS
    for i in range(h):
        for j in range(w):
            if island[i][j]:
                queue = deque()
                queue.append([i, j])
                island[i][j] = 0

                while queue:
                    loc = queue.popleft()

                    for k in range(8):
                        tmp_r = loc[0] + dx[k]
                        tmp_c = loc[1] + dy[k]

                        if 0 <= tmp_r < h and 0 <= tmp_c < w:
                            if island[tmp_r][tmp_c]:
                                queue.append([tmp_r, tmp_c])
                                island[tmp_r][tmp_c] = 0

                cnt += 1

    print(cnt)

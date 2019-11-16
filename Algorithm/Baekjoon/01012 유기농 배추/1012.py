# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

T = int(r_input())          # 테스트 케이스의 개수
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find_cabbage(search):           # 연결된 배추밭 찾기 (BFS)
    while search:
        loc = search.popleft()

        for i in range(4):
            temp_x = loc[0] + dx[i]
            temp_y = loc[1] + dy[i]

            if 0 <= temp_x < N and 0 <= temp_y < M:
                if field[temp_x][temp_y]:
                    field[temp_x][temp_y] = 0
                    search.append([temp_x, temp_y])


for _ in range(T):
    # M: 배추밭의 가로 길이, N: 배추밭의 세로 길이, K: 배추가 심어져있는 위치의 개수
    M, N, K = map(int, r_input().split())
    cnt = 0             # 필요한 최소 배추흰지렁이 수

    field = [[0]*M for _ in range(N)]

    for i in range(K):
        x, y = map(int, r_input().split())      # 배추의 위치
        field[y][x] = 1

    for i in range(N):
        for j in range(M):
            if field[i][j]:
                temp = deque()
                temp.append([i, j])
                field[i][j] = 0
                find_cabbage(temp)
                cnt += 1

    print(cnt)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())
cheese = [list(map(int, r_input().split())) for _ in range(N)]

cheese_location = []
empty_location = []

hour = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find_location():            # 빈 공간과 치즈의 공간 확인
    for i in range(N):
        for j in range(M):
            if i == 0 or i == N - 1 or j == 0 or j == M - 1:
                if cheese[i][j] == 0:
                    stack = [[i, j]]
                    cheese[i][j] = -1

                    while stack:
                        loc = stack.pop()

                        for k in range(4):
                            tmp_row = loc[0] + dx[k]
                            tmp_col = loc[1] + dy[k]

                            if 0 <= tmp_row < N and 0 <= tmp_col < M:
                                if cheese[tmp_row][tmp_col] == 0:
                                    cheese[tmp_row][tmp_col] = -1
                                    stack.append([tmp_row, tmp_col])

    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1:
                cheese_location.append([i, j])
            elif cheese[i][j] == 0:
                empty_location.append([i, j])


def melting():              # 녹는 부분 체크
    global cheese_location, cnt, hour

    tmp = []
    cnt = len(cheese_location)

    for loc in cheese_location:
        melted = 0
        for k in range(4):
            tmp_row = loc[0] + dx[k]
            tmp_col = loc[1] + dy[k]

            if 0 <= tmp_row < N and 0 <= tmp_col < M:
                if cheese[tmp_row][tmp_col] < 0:
                    melted = 1
                    break

        if not melted:
            tmp.append(loc)

    for loc in cheese_location:
        cheese[loc[0]][loc[1]] = -1

    for loc in tmp:
        cheese[loc[0]][loc[1]] = 1

    cheese_location = tmp
    hour += 1


def air_in():           # 공기가 들어오는 부분 체크
    global empty_location

    tmp = []

    for loc in empty_location:
        for k in range(4):
            tmp_row = loc[0] + dx[k]
            tmp_col = loc[1] + dy[k]

            if cheese[tmp_row][tmp_col] < 0:
                stack = [loc]
                cheese[loc[0]][loc[1]] = -1

                while stack:
                    loc2 = stack.pop()

                    for l in range(4):
                        tmp_row2 = loc2[0] + dx[l]
                        tmp_col2 = loc2[1] + dy[l]

                        if cheese[tmp_row2][tmp_col2] == 0:
                            cheese[tmp_row2][tmp_col2] = -1
                            stack.append([tmp_row2, tmp_col2])

                break

    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 0:
                tmp.append([i, j])

    empty_location = tmp


find_location()
cnt = len(cheese_location)

while cheese_location:
    melting()

    air_in()

print(hour)
print(cnt)

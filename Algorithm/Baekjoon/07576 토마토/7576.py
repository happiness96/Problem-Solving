# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 상자의 크기
M, N = map(int, r_input().split())
tomatoes = [list(map(int, r_input().split())) for _ in range(N)]
riped = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def setting():
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                for k in range(4):
                    tmp_row = i + dx[k]
                    tmp_col = j + dy[k]

                    if 0 <= tmp_row < N and 0 <= tmp_col < M:
                        if not tomatoes[tmp_row][tmp_col]:
                            riped.append((i, j))
                            break


def start():
    global result, riped

    if not riped:
        print(0)
        exit()

    while True:
        if not riped:
            result -= 1
            break

        tmp_riped = []

        while riped:
            tmp = riped.pop()

            for k in range(4):
                tmp_row = tmp[0] + dx[k]
                tmp_col = tmp[1] + dy[k]

                if 0 <= tmp_row < N and 0 <= tmp_col < M:
                    if tomatoes[tmp_row][tmp_col] == 0:
                        tomatoes[tmp_row][tmp_col] = 1
                        tmp_riped.append((tmp_row, tmp_col))

        riped = tmp_riped
        result += 1


def chk():
    for i in range(N):
        for j in range(M):
            if not tomatoes[i][j]:
                print(-1)
                exit()


result = 0

setting()
start()
chk()

print(result)

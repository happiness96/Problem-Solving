# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 미로의 행과 열
R, C = map(int, r_input().split())
maze = [list(r_input().rstrip()) for _ in range(R)]

fire = []

my_visit = [[0] * C for _ in range(R)]
fire_visit = [[0] * C for _ in range(R)]

my_loc = []


def setting():
    global my_loc
    # Setting
    for i in range(R):
        for j in range(C):
            loc = maze[i][j]
            if not loc == '.':
                if loc == 'F':
                    fire.append((i, j))
                    fire_visit[i][j] = 1

                elif loc == 'J':
                    my_loc = [(i, j)]
                    my_visit[i][j] = 1
                else:
                    my_visit[i][j] = 1
                    fire_visit[i][j] = 1


def start():
    global fire, my_loc
    cnt = 1
    flag = 0

    while my_loc:
        # 불이 퍼진다
        tmp_fire_loc = []

        while fire:
            tmp = fire.pop()

            for k in range(4):
                tmp_row = tmp[0] + dx[k]
                tmp_col = tmp[1] + dy[k]

                if 0 <= tmp_row < R and 0 <= tmp_col < C:
                    if not fire_visit[tmp_row][tmp_col]:
                        tmp_fire_loc.append((tmp_row, tmp_col))
                        fire_visit[tmp_row][tmp_col] = 1

        fire = tmp_fire_loc

        # 지훈이의 위치를 옮긴다
        tmp_my_loc = []

        while my_loc:
            tmp = my_loc.pop()

            for k in range(4):
                tmp_row = tmp[0] + dx[k]
                tmp_col = tmp[1] + dy[k]

                if 0 <= tmp_row < R and 0 <= tmp_col < C:
                    if not my_visit[tmp_row][tmp_col] and not fire_visit[tmp_row][tmp_col]:
                        tmp_my_loc.append((tmp_row, tmp_col))
                        my_visit[tmp_row][tmp_col] = 1

                else:
                    print(cnt)
                    exit()

        my_loc = tmp_my_loc

        cnt += 1

    print('IMPOSSIBLE')


setting()
start()

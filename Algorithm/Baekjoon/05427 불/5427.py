# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def start():            # 게임 스타트
    # 빌딩 지도의 너비와 높이
    w, h = map(int, r_input().split())
    building = [list(r_input().rstrip()) for _ in range(h)]

    cnt = 1
    fire = []

    my_visit = [[0] * w for _ in range(h)]
    fire_visit = [[0] * w for _ in range(h)]

    my_loc = []

    # Setting
    for i in range(h):
        for j in range(w):
            if not building[i][j] == '.':
                if building[i][j] == '*':
                    fire.append([i, j])
                    fire_visit[i][j] = 1

                elif building[i][j] == '@':
                    my_loc = [[i, j]]
                    my_visit[i][j] = 1
                else:
                    my_visit[i][j] = 1
                    fire_visit[i][j] = 1

    flag = 0

    while my_loc:
        # 불이 퍼진다
        tmp_fire_loc = []

        while fire:
            tmp = fire.pop()

            for k in range(4):
                tmp_row = tmp[0] + dx[k]
                tmp_col = tmp[1] + dy[k]

                if 0 <= tmp_row < h and 0 <= tmp_col < w:
                    if not fire_visit[tmp_row][tmp_col]:
                        tmp_fire_loc.append([tmp_row, tmp_col])
                        fire_visit[tmp_row][tmp_col] = 1

        fire = tmp_fire_loc

        # 상근이의 위치를 옮긴다. (현재 라운드에서 진행할 수 있는 위치 저장)
        tmp_my_loc = []

        while my_loc:
            tmp = my_loc.pop()

            for k in range(4):
                tmp_row = tmp[0] + dx[k]
                tmp_col = tmp[1] + dy[k]

                if 0 <= tmp_row < h and 0 <= tmp_col < w:
                    if not my_visit[tmp_row][tmp_col] and not fire_visit[tmp_row][tmp_col]:
                        tmp_my_loc.append([tmp_row, tmp_col])
                        my_visit[tmp_row][tmp_col] = 1

                else:
                    return cnt

        my_loc = tmp_my_loc

        cnt += 1

    return 'IMPOSSIBLE'


t = int(r_input())      # 테스트 케이스의 개수

for _ in range(t):
    print(start())

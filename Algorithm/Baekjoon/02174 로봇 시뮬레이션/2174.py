# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 땅의 가로, 세로 크기
A, B = map(int, r_input().split())
# N: 로봇의 개수, M: 명령의 개수
N, M = map(int, r_input().split())

# i번 로봇이 보고있는 방향 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
direction = [0] * (N + 1)
dir_n = {'N': 0, 'E': 1, 'S': 2, 'W': 3}

loc = [[-1, -1] for _ in range(N + 1)]      # 로봇들의 위치

for i in range(1, N + 1):
    x, y, d = list(map(str, r_input().rstrip().split()))
    direction[i] = dir_n[d]
    loc[i] = [int(x), int(y)]


def move(robot_n, order, cnt):      # 로봇 명령 수행하기
    if order == 'R':
        cnt %= 4
        direction[robot_n] += cnt

        if direction[robot_n] > 3:
            direction[robot_n] -= 4

    elif order == 'L':
        cnt %= 4
        direction[robot_n] -= cnt

        if direction[robot_n] < 0:
            direction[robot_n] += 4

    else:
        if direction[robot_n] == 0:
            dx = 0
            dy = 1
        elif direction[robot_n] == 1:
            dx = 1
            dy = 0
        elif direction[robot_n] == 2:
            dx = 0
            dy = -1
        else:
            dx = -1
            dy = 0

        tmp_loc = []

        for i in range(1, cnt + 1):
            tmp_loc = [loc[robot_n][0] + dx * i, loc[robot_n][1] + dy * i]

            if tmp_loc in loc:
                print('Robot', robot_n, 'crashes into robot', loc.index(tmp_loc))
                exit()

        if 0 < tmp_loc[0] <= A and 0 <= tmp_loc[1] <= B:
            loc[robot_n] = tmp_loc

        else:
            print('Robot', robot_n, 'crashes into the wall')
            exit()


for _ in range(M):
    a, b, c = list(map(str, r_input().rstrip().split()))
    move(int(a), b, int(c))

print('OK')

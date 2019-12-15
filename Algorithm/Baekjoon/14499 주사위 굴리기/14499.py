# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N, M: 지도의 크기, x, y: 주사위를 놓은 좌표, K: 명령의 개수
N, M, x, y, K = map(int, r_input().split())

die = [0] * 7
jido = [list(map(int, r_input().split())) for _ in range(N)]

loc1 = 1        # 현재 위치
loc2 = 3        # 동쪽의 위치
loc3 = 2        # 북쪽의 위치

# 이동 명령 1: 동쪽, 2: 서쪽, 3: 북쪽, 4: 남쪽
move = list(map(int, r_input().split()))
opposite = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}


def moving_east():          # 주사위 동쪽으로 이동
    global y, loc1, loc2
    y += 1

    if y >= M:
        y -= 1
        return 1

    loc1, loc2 = loc2, opposite[loc1]
    return 0


def moving_west():
    global y, loc1, loc2
    y -= 1

    if y < 0:
        y += 1
        return 1

    loc1, loc2 = opposite[loc2], loc1
    return 0


def moving_north():
    global x, loc1, loc3
    x -= 1

    if x < 0:
        x += 1
        return 1

    loc1, loc3 = loc3, opposite[loc1]
    return 0


def moving_south():
    global x, loc1, loc3
    x += 1

    if x >= N:
        x -= 1
        return 1

    loc1, loc3 = opposite[loc3], loc1
    return 0


for i in range(K):
    if move[i] == 1:
        if moving_east():
            continue
    elif move[i] == 2:
        if moving_west():
            continue
    elif move[i] == 3:
        if moving_north():
            continue
    else:
        if moving_south():
            continue

    print(die[opposite[loc1]])

    if jido[x][y]:
        jido[x][y], die[loc1] = 0, jido[x][y]

    else:
        jido[x][y] = die[loc1]

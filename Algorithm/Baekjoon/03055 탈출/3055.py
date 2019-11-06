# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline
sys.setrecursionlimit(10**6)

R, C = map(int, r().split())            # R행 C열

Hedge_row = 0       # 고슴도치의 좌표
Hedge_col = 0

cave_row = 0        # 동굴의 좌표
cave_col = 0

forest = {0: ['.']*(C+2), R+1: ['.']*(C+2)}     # 티떱숲

for i in range(1, R+1):     # 입력
    forest[i] = ['.']
    t = 1

    for j in r().rstrip():
        forest[i].append(j)

        if j == 'S':
            Hedge_row = i
            Hedge_col = t

        if j == 'D':
            cave_row = i
            cave_col = t

        t += 1

    forest[i].append('.')


def fill_water(water_r, water_c):       # 물 채우기
    if 1 <= water_r <= R and 1 <= water_c <= C:
        if not forest[water_r][water_c] in 'XD':        # 물이 돌을 만나거나 비버의 굴을 만나지 않는 경우
            forest[water_r][water_c] = '*'


def next_stage():           # 1분이 지난 후 (물의 상태)
    water = []

    for i in range(1, R+1):
        for j in range(1, C+1):
            if forest[i][j] == '*':
                water.append([i, j])

    for w in water:
        fill_water(w[0]-1, w[1])
        fill_water(w[0]+1, w[1])
        fill_water(w[0], w[1]-1)
        fill_water(w[0], w[1]+1)


def find_cave(h_location, minute):       # 비버의 굴을 찾아서 (DP)
    next_stage()  # 1분 후 물이 차오르는 곳 채우기

    next_search = []  # 다음 탐색

    for location in range(len(h_location)):
        h_row = h_location[location][0]
        h_col = h_location[location][1]

        if 1 <= h_row <= R and 1 <= h_col <= C:

            if forest[h_row][h_col] == 'D':     # 비버의 굴을 찾았다면 종료
                print(minute)
                exit()

            temp = [[h_row-1, h_col], [h_row+1, h_col], [h_row, h_col-1], [h_row, h_col+1]]

            for loc in temp:
                if not forest[loc[0]][loc[1]] in 'X*':
                    if not loc in next_search:
                        next_search.append(loc)
    if next_search:
        find_cave(next_search, minute + 1)


find_cave([[Hedge_row, Hedge_col]], 0)

print('KAKTUS')

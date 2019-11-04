# -*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(r())            # N x N
color1 = {0: ['.']*(N+2), N+1: ['.']*(N+2)}             # 적록색약이 아닌 사람이 봤을 때
color2 = {0: ['.']*(N+2), N+1: ['.']*(N+2)}             # 적록색약인 사람이 봤을 때
color1_area = 0
color2_area = 0


def find_area(area, row, col, rgb):         # 같은 구역 찾기
    if area[row][col] == rgb:
        area[row][col] = '.'

        find_area(area, row-1, col, rgb)
        find_area(area, row+1, col, rgb)
        find_area(area, row, col-1, rgb)
        find_area(area, row, col+1, rgb)


for i in range(1, N+1):
    color1[i] = ['.']
    color2[i] = ['.']

    for c in r().rstrip():
        color1[i].append(c)

        if c == 'G':
            color2[i].append('R')

        else:
            color2[i].append(c)

    color1[i].append('.')
    color2[i].append('.')

for i in range(1, N+1):
    for j in range(1, N+1):
        if color1[i][j] != '.':
            find_area(color1, i, j, color1[i][j])
            color1_area += 1

        if color2[i][j] != '.':
            find_area(color2, i, j, color2[i][j])
            color2_area += 1

print(color1_area, color2_area)

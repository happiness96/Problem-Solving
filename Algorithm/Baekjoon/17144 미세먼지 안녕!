# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

R, C, T = map(int, r_input().split())       # R x C 격자판, T: 시간

room = {}                   # 구사과의 방
aircon = []                 # 공기청정기의 위치

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(R):
    room[i] = list(map(int, r_input().split()))
    if room[i][0] == -1:
        aircon.append([i, 0])


def dirt_spread():
    plus = []
    minus = []

    for i in range(R):
        for j in range(C):

            if room[i][j] > 4:  # 미세 먼지가 있는 공간일 경우
                for k in range(4):
                    row = i + dx[k]
                    col = j + dy[k]
                    cnt = 0
                    if 0 <= row < R and 0 <= col < C and [row, col] not in aircon:
                        cnt += 1
                        plus.append([row, col, room[i][j] // 5])
                    minus.append([i, j, room[i][j] // 5 * cnt])

    while plus:
        a_tmp = plus.pop()
        room[a_tmp[0]][a_tmp[1]] += a_tmp[2]

    while minus:
        a_tmp = minus.pop()
        room[a_tmp[0]][a_tmp[1]] -= a_tmp[2]


def air_conditional():
    temp1 = 0
    temp2 = 0

    for i in range(1, C):
        room[aircon[0][0]][i], temp1 = temp1, room[aircon[0][0]][i]
        room[aircon[1][0]][i], temp2 = temp2, room[aircon[1][0]][i]

    for i in range(aircon[0][0]-1, -1, -1):
        room[i][-1], temp1 = temp1, room[i][-1]

    for i in range(aircon[1][0]+1, R):
        room[i][-1], temp2 = temp2, room[i][-1]

    for i in range(C-2, -1, -1):
        room[0][i], temp1 = temp1, room[0][i]
        room[R-1][i], temp2 = temp2, room[R-1][i]

    for i in range(1, aircon[0][0]):
        room[i][0], temp1 = temp1, room[i][0]

    for i in range(R-2, aircon[1][0], -1):
        room[i][0], temp2 = temp2, room[i][0]


for _ in range(T):
    dirt_spread()
    air_conditional()

result = 0
for i in range(R):
    result += sum(room[i])

print(result + 2)

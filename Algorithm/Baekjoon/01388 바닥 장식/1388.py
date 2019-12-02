# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 방 바닥의 세로 길이, M: 가로 길이
N, M = map(int, r_input().split())

room = []

for i in range(N):
    room.append(list(r_input().rstrip()))

cnt = 0


def chk_col(x, y):
    for col in range(x + 1, N):
        if room[col][y] == '|':
            room[col][y] = 0

        else:
            return


for i in range(N):
    conti = 0

    for j in range(M):
        if room[i][j] and room[i][j] == '-':
            conti += 1

            if j == M - 1:
                cnt += 1

        elif conti:
            cnt += 1
            conti = 0

        if room[i][j] == '|':
            chk_col(i, j)
            cnt += 1

        room[i][j] = 0

print(cnt)

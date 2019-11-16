# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # N: 방의 크기
room = []
garo = 0
sero = 0

for i in range(N):
    room.append(list(r_input().rstrip()))

temp1 = 0
for i in range(N):
    for j in range(N):
        if room[i][j] == '.':
            temp1 += 1
        else:
            if temp1 > 1:
                garo += 1
            temp1 = 0
    if temp1 > 1:
        garo += 1
    temp1 = 0

temp2 = 0
for j in range(N):
    for i in range(N):
        if room[i][j] == '.':
            temp2 += 1
        else:
            if temp2 > 1:
                sero += 1
            temp2 = 0
    if temp2 > 1:
        sero += 1
    temp2 = 0

print(garo, sero)

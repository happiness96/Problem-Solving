# -*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # N days
sun_height = {}

for i in range(N):
    sun_height[i] = list(map(int, r().split()))

if sun_height[0][0] < sun_height[0][1]:
    if sun_height[0][0] < sun_height[1][0]:         # 0도 돌아간 경우
        for i in range(N):
            for sun_flower in sun_height[i]:
                print(sun_flower, end=' ')
            print()

    else:               # 180도 돌아간 경우
        for j in range(N):
            for i in range(N):
                print(sun_height[N-i-1][j], end=' ')
            print()

else:
    if sun_height[0][0] < sun_height[1][0]:     # 90도 돌아간 경우
        for j in range(N):
            for i in range(N):
                print(sun_height[i][N-j-1], end=' ')
            print()

    else:               # 270도 돌아간 경우
        for i in range(N):
            for j in range(N):
                print(sun_height[N-i-1][N-j-1], end=' ')
            print()

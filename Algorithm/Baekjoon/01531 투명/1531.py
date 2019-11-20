# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())          # N개의 불투명한 종이

pic = [[0] * 101 for _ in range(101)]       # 그림

for i in range(N):
    x1, y1, x2, y2 = map(int, r_input().split())

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            pic[x][y] += 1

cnt = 0
for i in range(1, 101):
    for j in range(1, 101):
        if pic[i][j] > M:
            cnt += 1

print(cnt)

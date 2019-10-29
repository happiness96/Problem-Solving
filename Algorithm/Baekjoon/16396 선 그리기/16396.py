#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())            # N: 선의 개수
line = [0] * 10001

for i in range(N):
    x, y = map(int, r().split())
    line[x:y] = [1] * (y-x)

print(line.count(1))

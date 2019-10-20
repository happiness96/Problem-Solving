#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # N: 색종이의 가로, 세로 길이

result = 0

for i in range(N):
    result += sum(list(map(int,r().split())))

print(result)

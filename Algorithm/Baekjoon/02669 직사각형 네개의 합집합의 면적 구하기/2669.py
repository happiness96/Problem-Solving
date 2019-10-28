#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

area = {}        # 평면

for i in range(1, 101):
    area[i] = [0] * 101
    
result = 0

for i in range(4):          # 4개의 직사각형
    x1, y1, x2, y2 = map(int, r().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            if area[y][x] == 0:
                area[y][x] = 1
                result +=1

print(result)

#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

paper = {}          # 도화지
N = int(r())        # 색종이의 수

for i in range(100):
    paper[i] = [0] * 100

for i in range(N):
    a, b = map(int,r().split())     # a: 색종이와 도화지의 왼쪽 변 사이의 거리, b: 색종이와 도화지의 아래쪽 변 사이의 거리
    
    for j in range(a, a+10):
        for k in range(b, b+10):
            paper[j][k] = 1

area = 0            # 검은색 영역의 넓이
for i in range(100):
    area += paper[i].count(1)

print(area)

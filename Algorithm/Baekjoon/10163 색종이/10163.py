#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # 색종이의 장수
paper = {}      # 평면 종이

for i in range(101):
    paper[i] = [0] * 101

for i in range(1, N+1):
    x, y, w, h = map(int, r().split())
    for b in range(y, y+h):
        for a in range(x, x+w):
            paper[a][b] = i         # 종이 순서대로 덮기

cnt = [0] * (N+1)

for y in range(101):
    for x in range(101):
        cnt[paper[x][y]] += 1

for i in range(1, N+1):
    print(cnt[i])

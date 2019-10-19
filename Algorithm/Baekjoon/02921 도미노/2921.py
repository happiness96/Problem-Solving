#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # 도미노의 크기
dot = 0             # 점의 개수

for i in range(1, N+1):
    dot += i * (i+1)    # 하단부
    dot += i * (1 + i) // 2     # 상단부

print(dot)

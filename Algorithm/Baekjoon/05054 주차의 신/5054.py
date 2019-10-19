#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

t = int(r())        # t: 테스트 케이스 개수

for i in range(t):
    n = int(r())        # n: 방문할 상점의 수
    x = list(map(int,r().split()))      # 상점의 위치
    
    print(2 * (max(x) - min(x)))

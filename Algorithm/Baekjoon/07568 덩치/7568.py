#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # N: 전체 사람의 수
Big = []            # 덩치

for i in range(N):
    weight, height = map(int, r().split())      # 몸무게, 키
    Big.append([weight, height])

for you in Big:
    w, h = you[0], you[1]
    rank = 1         # 등수
    
    for comp in Big:
        if comp[0] > w and comp[1] > h:         # 자신보다 덩치가 큰 사람이 있으면
            rank += 1
    
    print(rank, end=' ')

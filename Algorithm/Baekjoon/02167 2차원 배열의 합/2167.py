#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N,M = map(int,r().split())      # 배열의 크기 (N x M)

array_set = {}                  # 저장할 배열

for i in range(1, N+1):
    array_set[i] = [0] + list(map(int,r().split()))

K = int(r())        # 합을 구할 부분의 개수

for quest in range(K):
    i, j, x, y = map(int,r().split())       # i행 j열부터 x행 y열까지
    total = 0           # 합계
    
    for t in range(i, x + 1):
        total += sum(array_set[t][j:y+1])
        
    print(total)

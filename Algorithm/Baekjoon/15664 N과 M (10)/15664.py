#-*- encoding: utf-8 -*-
import sys
from itertools import combinations
r=sys.stdin.readline

N, M = map(int, r().split())

l = sorted([num for num in map(int,r().split())])

for i in range(N):
    l[i] = str(l[i])

printed = {}            # 이미 출력된 것들
for per in combinations(l, M):
    result = ' '.join(per)
    
    if not result in printed:
        print(result)
    
    printed[result] = 0

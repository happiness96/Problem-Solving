#-*- encoding: utf-8 -*-
import sys
from itertools import combinations
r=sys.stdin.readline

N, M = map(int, r().split())

l = sorted([num for num in map(int,r().split())])

for i in range(N):
    l[i] = str(l[i])
    
for per in combinations(l, M):
    print(' '.join(per))

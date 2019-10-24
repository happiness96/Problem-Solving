#-*- encoding: utf-8 -*-
import sys
from itertools import combinations
r=sys.stdin.readline

N, M = map(int, r().split())

l = [str(num) for num in range(1, N+1)]

for per in combinations(l, M):
    print(' '.join(per))

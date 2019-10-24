#-*- encoding: utf-8 -*-
import sys
from itertools import permutations
r=sys.stdin.readline

N, M = map(int, r().split())

l = [str(num) for num in range(1, N+1)]

for per in permutations(l, M):
    print(' '.join(per))

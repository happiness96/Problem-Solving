# -*- encoding: utf-8 -*-
import sys
from itertools import combinations
r_input = sys.stdin.readline

N = int(r_input())          # 수열의 크기

S = sorted(map(int, r_input().split()))         # 집합

chk = [0] + [1] * 2000000

for i in range(1, N+1):
    for nums in combinations(S, i):
        chk[sum(nums)] = 0

for i in range(2000002):
    if chk[i]:
        print(i)
        exit()

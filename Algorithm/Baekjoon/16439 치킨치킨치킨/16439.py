# -*- encoding: utf-8 -*-
import sys
from itertools import combinations
r_input = sys.stdin.readline

# N: 고리 회원의 수, M: 치킨 종류의 수
N, M = map(int, r_input().split())
total = 0

satisfy = {}            # 치킨의 만족도

for i in range(N):
    satisfy[i] = list(map(int, r_input().split()))

chicken_num = [n for n in range(M)]

for select in combinations(chicken_num, 3):
    tmp = 0

    for i in range(N):
        tmp += max(satisfy[i][select[0]], satisfy[i][select[1]], satisfy[i][select[2]])

    total = max(total, tmp)

print(total)

# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

parents = {}        # 행복한 사람들의 부모
N = int(r())        # N: 사람의 수

for i in range(1, N+1):
    mom, dad = map(int, r().split())

    if mom != 0 and dad != 0:
        parents[i] = [mom, dad]

M = int(r())        # 사망하거나 미국에 간 사람의 수
exc = list(map(int, r().split()))       # 사망하거나 미국에 간 사람들

happy = len(parents)

for child in parents:
    if child in exc or parents[child][0] in exc or parents[child][1] in exc:
        happy -= 1

print(happy)

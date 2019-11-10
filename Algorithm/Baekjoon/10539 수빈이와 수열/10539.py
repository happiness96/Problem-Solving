# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())      # 수열의 길이
total = 0               # 수열의 누적 총합
cnt = 1                 # 수열의 누적 개수

for b in map(int, r_input().split()):
    temp = b * cnt
    print(temp - total, end=' ')
    total = temp
    cnt += 1

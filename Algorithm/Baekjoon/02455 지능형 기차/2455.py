# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

result = 0          # 기차에 사람이 가장 많을 때 사람 수
cnt = 0             # 현재 기차에 타고 있는 사람 수

for i in range(4):
    A, B = map(int, r_input().split())          # A명이 내리고 B명이 탑승
    cnt -= A
    cnt += B

    result = max(cnt, result)

print(result)

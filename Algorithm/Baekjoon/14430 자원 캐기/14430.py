# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())          # WOOK이 탐사할 영역의 세로 길이, 가로 길이

line = [0] * M              # DP

for i in range(N):
    new_line = list(map(int, r_input().split()))
    line[0] += new_line[0]

    for j in range(1, M):
        line[j] = max(line[j-1], line[j]) + new_line[j]

print(line[-1])

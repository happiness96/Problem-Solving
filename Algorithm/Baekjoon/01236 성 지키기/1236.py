# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())      # 성의 크기
castle = {}

garo = 0            # 가로 줄에 있는 경비원의 수
sero = 0            # 세로 줄에 있는 경비원의 수

for i in range(N):
    castle[i] = r_input().rstrip()
    if 'X' in castle[i]:
        garo += 1

for i in range(M):
    for j in range(N):
        if castle[j][i] == 'X':
            sero += 1
            break

print(max(N-garo, M-sero))

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

drawing = {}            # 그림들

N = int(r_input())          # 그림의 개수

result = []         # 가장 비슷한 두 그림의 번호
min_gap = 2160

for i in range(N):
    drawing[i] = [list(r_input().rstrip()) for _ in range(5)]

for i in range(N-1):
    for j in range(i+1, N):
        gap = 0

        for a in range(5):
            for b in range(7):
                if drawing[i][a][b] != drawing[j][a][b]:
                    gap += 1

        if gap < min_gap:
            min_gap = gap
            result = [i, j]

print(result[0]+1, result[1]+1)

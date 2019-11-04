# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

A, B = map(int, r().split())        # A: 현재 주파수, B: 듣고싶은 주파수
library = 0            # 즐겨찾기
gap = 1000          # 지정된 즐겨찾기와의 최소 차

N = int(r())

for i in range(N):
    lib = int(r())
    temp = abs(B - lib)         # 해당 즐겨찾기와 듣고싶은 주파수의 차

    if temp < gap:
        gap = temp
        library = lib

print(min(abs(B-A), abs(B-library) + 1))

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# R: 빨간색 타일의 개수, B: 갈색 타일의 개수
R, B = map(int, r_input().split())

total = R + B

W = 3

while True:
    if not total % W:
        L = total // W

        if (L - 2) * (W - 2) == B:
            print(L, W)
            break

    W += 1

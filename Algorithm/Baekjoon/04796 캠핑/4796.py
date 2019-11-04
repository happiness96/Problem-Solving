# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

i = 1
while True:
    # 연속하는 P일 중 L일만 캠핑장을 사용할 수 있다.
    # 강산이는 휴가를 V일 동안 받았다.
    L, P, V = map(int, r().split())

    if L == 0:
        break

    print('Case ' + str(i) + ': ' + str(L * (V // P) + min(V % P, L)))
    i += 1

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 줄의 개수

for i in range(N):
    print('*' * (N - i))

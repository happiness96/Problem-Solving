# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, L, D = map(int, r_input().split())
max_len = N*(L+5)

ring = [] * max_len

for i in range(N):
    ring[i*(L+5): (i+1)*(L+5)] = [1]*L + [0]*5

tmp = 0
while 1:
    sec = D * tmp
    if sec >= max_len or ring[sec] == 0:
        print(sec)
        break

    tmp += 1

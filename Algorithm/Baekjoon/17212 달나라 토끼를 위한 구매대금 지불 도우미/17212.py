# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())      # 토끼가 합법적으로 내야하는 금액

coin = [7, 5, 2, 1]
counts = [0, 0, 0, 0]

cnt = 0

for i in range(4):
    cnt += N // coin[i]
    counts[i] = N // coin[i]
    N %= coin[i]

while counts[0] and counts[2] and counts[3]:
    counts[0] -= 1
    counts[2] -= 1
    counts[3] -= 1
    cnt -= 1

print(cnt)

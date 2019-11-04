# -*- encoding: utf-8 -*-
import sys
import math
r = sys.stdin.readline

N = int(r())
pool = {}

for i in range(N):
    pool[i] = list(map(int, r().split()))

for i in range(int(math.log2(N))):
    for row in range(N//2):
        for col in range(N//2):
            temp = [pool[2*row][2*col], pool[2*row+1][2*col+1], pool[2*row+1][2*col], pool[2*row][2*col+1]]
            pool[row][col] = sorted(temp)[2]

    N //= 2
print(pool[0][0])

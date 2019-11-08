# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

N = int(r())        # 숫자의 개수
total = 0           # 숫자의 총합

num = r().rstrip()

for i in range(N):
    total += int(num[i])

print(total)

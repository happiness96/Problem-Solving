#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

m = int(r())
result = [0] * m
temp = 1 / m
temp_list = {}

for i in range(1, m):
    temp_list[i] = float('%.07f' % (temp * i))
temp_list[m] = 1

for num in map(float, r().split()):

    for i in range(1, m+1):
        if num < temp_list[i]:
            result[i-1] += 1
            break
    
for c in result:
    print(c, end=' ')

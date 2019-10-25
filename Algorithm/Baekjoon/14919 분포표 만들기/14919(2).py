#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

m = int(r())
result = [0] * m
temp = 1 / m

for num in map(float, r().split()):
    result[int(num / temp + 0.00000001)] += 1
    
for c in result:
    print(c, end=' ')

#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

l = {}
N = int(r())

for i in range(N):
    num = int(r())
    if num in l:
        l[num] += 1
    else:
        l[num] = 1

for number in sorted(l):
    print((str(number)+'\n') * l[number], end='')

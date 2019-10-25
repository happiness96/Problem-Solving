#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # N: The size of complete set
dots = 0

for i in range(1, N+1):
    dots += i*(i+1)     # down
    dots += i*(1+i)//2  # up

print(dots)

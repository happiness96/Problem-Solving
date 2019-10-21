#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

while True:
    N = int(r())        # The number of tickets
    
    if N == 0:
        break
    
    numbers = [0]*49
    
    for i in range(N):
        for j in map(int,r().split()):
            numbers[j-1] += 1
    
    print('No' if 0 in numbers else 'Yes')

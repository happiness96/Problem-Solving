#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

n = int(r())            # The number of problem

for i in range(n):
    m = int(r())        # m words
    sheep_list = list(map(str, r().rstrip().split()))
    cnt = 0
    
    for sheep in sheep_list:        # counting sheep
        if sheep == 'sheep':
            cnt += 1
    
    print('Case ' + str(i+1) + ': This list contains', cnt, 'sheep.')
    print()

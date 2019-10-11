#-*- encoding: utf-8 -*-
import sys
from math import log
r=sys.stdin.readline

N = int(r())            # The number of data set

for i in range(N):
    chem, equals, estimate = map(str,r().rstrip().split())
    pH = 0              # pH
    
    if chem == 'H':
        pH = -log(float(estimate), 10)
        
    elif chem == 'OH': 
        pH = 14 + log(float(estimate), 10)
    
    print('%.2f' % pH)

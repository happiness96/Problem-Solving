#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())            # The number of test case

for t in range(N):
    C = int(r())            # The amount of credit
    I = int(r())            # The number of itmes in the store
    P = list(map(int,r().split()))          # price of items
    
    for a in range(I):
        if C-P[a] in P[a+1:]:
            print('Case #' + str(t+1) + ': ' + str(a+1), str(P[a+1:].index(C-P[a])+2+a))
            break

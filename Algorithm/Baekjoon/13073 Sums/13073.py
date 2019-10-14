#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

t = int(r())            # t: The number of test cases

for i in range(t):
    N = int(r())
    
    # S1: the sum of first N positive integer
    # S2: the sum of first N odd integer
    # S3: the sum of first N even integer
    
    S1 = N*(1+N)//2       # 등차수열 합 공식
    S2 = N*(2*N)//2
    S3 = N*(2+(2*N))//2
    
    print(S1, S2, S3)

#-*- encoding: utf-8 -*-
import sys 
r=sys.stdin.readline

N, M = map(int, r().split())        # N x M
l = sorted([num for num in map(int,r().split())])


def N_and_M(node, result):          # DFS 방식
    result.append(str(l[node]))
    
    if len(result) == M:
        print(' '.join(result))
    
    else:
        for i in range(node+1, N):
            N_and_M(i, result)
    
    result.pop()


for i in range(N):
    N_and_M(i, [])

#-*- encoding: utf-8 -*-
import sys 
r=sys.stdin.readline

N, M = map(int, r().split())        # N x M


def N_and_M(node, result):          # DFS 방식
    result.append(str(node))
    
    if len(result) == M:
        print(' '.join(result))
    
    else:
        for i in range(node+1, N+1):
            N_and_M(i, result)
    
    result.pop()


for i in range(1, N+1):
    N_and_M(i, [])

#-*- encoding: utf-8 -*-
import sys 
r=sys.stdin.readline

N, M = map(int, r().split())        # N x M
l = sorted([num for num in map(int,r().split())])
perm = [True] * N       # False: 방문 한 노드


def N_and_M(node, result):          # DFS 방식
    result.append(str(l[node]))
    perm[node] = False
    
    if len(result) == M:
        print(' '.join(result))
    
    else:
        for i in range(N):
            if perm[i]:
                N_and_M(i, result)
    
    perm[node] = True
    result.pop()


for i in range(N):
    N_and_M(i, [])

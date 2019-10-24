#-*- encoding: utf-8 -*-
import sys 
r=sys.stdin.readline

N, M = map(int, r().split())        # N x M
l = sorted([num for num in map(int,r().split())])
permut = [True] * N             # False: 이미 방문한 노드
printed = {}                # 이미 출력된 것들


def N_and_M(node, result):          # DFS 방식
    result.append(str(l[node]))
    permut[node-1] = False
    
    if len(result) == M:
        temp = ' '.join(result)
        if not temp in printed:
            print(temp)
        printed[temp] = 0
    
    else:
        for i in range(N):
            if permut[i-1]:
                N_and_M(i, result)
        
    permut[node-1] = True
    result.pop()


for i in range(N):
    N_and_M(i, [])

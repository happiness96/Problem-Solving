#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N, M = map(int, r().split())        # 1부터 N까지 중복 없이  M개를 고른 수열

visit = [False] * (N+1)
result = [0]


def n_and_m(num):
    result.append(num)
    
    if len(result) == M+1:
        for c in result[1:]:
            print(c, end=' ')
        print()
    
    else:
        visit[num] = True
        for i in range(1, N+1):
            if not visit[i]:
                n_and_m(i)
        visit[num] = False
    result.pop()


for i in range(1, N+1):
    n_and_m(i)

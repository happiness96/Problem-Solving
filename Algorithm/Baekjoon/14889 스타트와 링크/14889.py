#-*- encoding: utf-8 -*-
import sys
from itertools import combinations 
r=sys.stdin.readline

N = int(r())        # 인원 수
people = [num for num in range(1, N+1)]

S = {}              # 능력치
result = []

for i in range(1, N+1):     # 능력치 입력
    S[i] = [0] + list(map(int, r().split()))

for start_team in list(combinations(people, N//2)):
    start = 0           # 스타트 팀 점수
    link = 0            # 링크 팀 점수
    
    if start_team[0] != 1: break
    
    for i in range(1, N+1):
        if i in start_team:
            for j in start_team:
                start += S[i][j]
                
        elif not i in start_team:
            for j in range(1, N+1):
                if not j in start_team:
                    link += S[i][j]
                    
    diff = abs(start-link)
    
    if diff :
        result.append(diff)
    else:
        print(0)
        exit()

print(min(result))

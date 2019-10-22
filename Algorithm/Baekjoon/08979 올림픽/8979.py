#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N, K = map(int,r().split())         # N: 국가의 수. K: 등수를 알고 싶은 국가
rank = {}

for i in range(N):      # 국가 번호, 금메달, 은메달, 동매달
    country_num, gold, silver, bronze = map(int,r().split())

    if not gold in rank:
        rank[gold] = {}
    
    if not silver in rank[gold]:
        rank[gold][silver] = {}
        
    if not bronze in rank[gold][silver]:
        rank[gold][silver][bronze] = []
    
    rank[gold][silver][bronze].append(country_num)
    
cnt = 0         # K보다 더 잘한 나라의 수

for G in sorted(rank, reverse = True):
    for S in sorted(rank[G], reverse = True):
        for B in sorted(rank[G][S], reverse = True):
            if K in rank[G][S][B]:
                print(cnt + 1)
                break
            else:
                cnt += len(rank[G][S][B])

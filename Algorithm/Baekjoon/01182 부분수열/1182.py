#-*- encoding: utf-8 -*-
import sys
from itertools import combinations
r=sys.stdin.readline

N, S = map(int,r().split())     # N개의 정수로 이루어진 수열이 있을 때 합이 S가 되는 부분 수열
cnt = 0 

numbers = list(map(int, r().split()))

for i in range(1, N+1):
    for l in list(combinations(numbers, i)):
        if sum(l) == S:         # 만약 부분 수열의 합이 S가 된다면
            cnt += 1
            
print(cnt)

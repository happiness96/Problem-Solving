#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # 테스트 케이스의 개수

for i in range(T):
    n, m = map(int,r().split())
    total = (m-n+1)*(m+n)//2        # 등차 수열
    
    print('Scenario #' + str(i+1) + ':')
    print(total)
    print()

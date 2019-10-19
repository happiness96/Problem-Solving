#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

M = int(r())            # M: 벨트의 개수

result = 1
rotate = 0
for i in range(M):
    # a, b = i번째 벨트가 a번 회전할 때 i+1번째 벨트가 b번 회전
    # s: i번째 벨트가 (0: 안꼬인 형태, 1: 꼬인 형태)
    a,b,s = map(int,r().split())
    result = result * b // a
    
    if s == 1:
        rotate = abs(rotate - 1)
        
print(rotate, result)

#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

n = int(r())        # The number of child recited

recited = {}
m = 0               # max number

for i in range(n):
    num = int(r())
    recited[num] = 0
    
    if i == n-1:
        m = num

if m == n:          # 모두 다 제대로 불렀을 경우
    print('good job')
    exit()
    
for i in range(1, m+1):            # 제대로 안 불렀을 경우
    if not i in recited:
        print(i)

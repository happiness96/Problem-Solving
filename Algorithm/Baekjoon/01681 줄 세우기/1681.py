#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N, L = map(int,r().split())         # N: 학생들의 수, L: 포함되지 않길 원하는 수

count = 0       # 번호가 주어진 학생들의 수
number = 1

while 1:
    if str(L) in str(number):   # number에 L이 포함되어 있다면 패스
        number += 1
        continue
    count += 1
    
    if count == N: break
    
    number += 1
    
print(number)

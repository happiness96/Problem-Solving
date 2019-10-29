#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

memo = {}           # 시침 각도에 따른 분침 각도 저장
min = 0

for i in range(360):
    memo[i] = min
    min += 12
    if min  >= 360:
        min -= 360

theta1, theta2 = map(int,r().split())

print('O' if memo[theta1] == theta2 else 'X')

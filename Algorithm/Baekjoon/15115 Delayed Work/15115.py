#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

# K: 페인팅이 끝나기까지 걸린 날
# P: Penalty
# X: Salary
K, P, X = map(int,r().split())
result = []

for painters in range(1, 10001):
    coop = K/painters
    pay = X * painters + coop * P
    result.append(pay)

print('%.03f' % min(result))

#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

A, B = map(int,r().split())
C, D = map(int,r().split())

result = []

result.append(A/C + B/D)
result.append(C/D + A/B)
result.append(D/B + C/A)
result.append(B/A + D/C)

print(result.index(max(result)))

#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

A, B = map(int, r().split())

if A > B:
    A, B = B, A

print((B-A+1)*(A+B)//2)         # 등차수열 합 공식

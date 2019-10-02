#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

# N: 여름 일 수, T: 스타후르츠가 자라는데 걸리는 시간
# C: 스타후르츠를 심을 수 있는 칸의수, P: 스타후르츠 개당 가격
N,T,C,P = map(int,r().split())

froots = N//T       # 여름 기간동안 한 칸에서 키울 수 있는 스타후르츠 개수
if N%T==0: froots-=1

print(froots * C * P)

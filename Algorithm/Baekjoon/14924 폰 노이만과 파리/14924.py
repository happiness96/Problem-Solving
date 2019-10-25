#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

S, T, D = map(int, r().split())         # S: 기차의 속도, T: 파리의 속도, D: 처음 두 기차 사이의 거리

# 간단한 논리
time = D / (S * 2)      # 두 기차가 만나는 시간
print(int(T * time))

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

T = int(r_input())          # 테스트 케이스의 개수

facto = [1]

for i in range(1, 31):
    facto.append(facto[-1] * i)

for _ in range(T):
    # N: 강의 서쪽에 있는 사이트의 수, M: 강의 동쪽에 있는 사이트의 수
    N, M = map(int, r_input().split())

    # M개의 사이트 중 N개를 뽑은 조합
    print(facto[M] // (facto[N] * facto[M - N]))

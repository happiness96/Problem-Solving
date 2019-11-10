# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 문제의 수
S = r_input().rstrip()      # 채점 결과

score = 0               # 최종 결과
bonus = 0               # 보너스 점수

for i in range(N):
    if S[i] == 'X':     # 문제를 틀렸을 경우
        bonus = 0

    else:               # 문제를 맞췄을 경우
        score += i+1 + bonus
        bonus += 1

print(score)

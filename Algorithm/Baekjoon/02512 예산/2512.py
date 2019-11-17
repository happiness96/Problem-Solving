# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 지방의 수
t_N = N

budget = list(map(int, r_input().split()))          # 각 지방들의 예산 요청 금액

maximum = int(r_input())            # 총액 상한선

if maximum >= sum(budget):
    print(max(budget))
    exit()

while True:
    avr = maximum // N
    cnt = 0         # 예산 요청 평균보다 적은 지방의 개수

    for i in range(t_N):
        if budget[i] != 0 and budget[i] < avr:
            cnt += 1
            maximum -= budget[i]
            N -= 1
            budget[i] = 0

    if cnt == 0:
        print(avr)
        break

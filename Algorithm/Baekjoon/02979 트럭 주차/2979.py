# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 한 대당 주차 가격 (A: 한 대 주차, B: 두 대 주차, C: 세 대 주차)
cost = [0] + list(map(int, r_input().split()))

time = [0] * 101
total = 0

for i in range(3):
    # 차가 들어온 시간, 차가 떠난 시간
    start, over = map(int, r_input().split())

    for t in range(start, over):
        time[t] += 1

for t in time:
    total += cost[t] * t

print(total)

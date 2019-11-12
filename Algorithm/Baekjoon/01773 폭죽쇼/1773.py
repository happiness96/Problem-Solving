# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 학생의 수, C: 폭죽쇼가 끝나는 시간
N, C = map(int, r_input().split())
sec = [0] * (C+1)
dup = []

for i in range(N):
    cycle = int(r_input())      # 폭죽이 터지는 주기
    
    if cycle in dup:
        continue

    dup.append(cycle)

    t = 1

    while cycle * t <= C:
        sec[cycle * t] = 1
        t += 1

print(sec.count(1))

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())      # 시험장의 개수
A = tuple(map(int, r_input().split()))      # 각 시험장에 있는 응시자의 수
# B: 총감독관이 한 방에서 감시할 수 있는 응시자의 수, C: 부감독관이 한 방에서 감시할 수 있는 응시자의 수
B, C = map(int, r_input().split())

total = 0       # 감독관의 수

for a in A:
    # 총 감독관 투입
    total += 1
    a -= B
    
    if a > 0:
        # 부감독관 투입
        total += a // C

        if a % C:
            total += 1

print(total)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # Fisherman caught N tunas last night
total_value = 0             # total value of tunas

X = int(r_input())          # The number from the task

for i in range(N):
    P1, P2 = map(int, r_input().split())

    if abs(P1 - P2) <= X:
        total_value += max(P1, P2)
        
    else:
        total_value += int(r_input())       # P3

print(total_value)

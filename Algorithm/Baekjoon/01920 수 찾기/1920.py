# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())
numbers = {}

for num in map(int, r_input().split()):
    numbers[num] = 0

M = int(r_input())
for num in map(int, r_input().split()):
    print(1 if num in numbers else 0)

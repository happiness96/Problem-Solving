# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())      # N: 숫자의 개수
numbers = []

for i in range(N):
    numbers.append(int(r_input()))

numbers.sort(reverse = True)

while numbers:
    print(numbers.pop())

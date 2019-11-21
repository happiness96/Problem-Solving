# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 입력을 받을 정수의 개수
num_list = list(map(int, r_input().split()))        # 정수 리스트

summation = sum(num_list)
total = 0

for num in num_list:
    summation -= num
    total += num * summation

print(total)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

n = int(r_input())
number_list = list(map(int, r_input().split()))

for i in range(1, n):
    number_list[i] = max(number_list[i - 1] + number_list[i], number_list[i])

print(max(number_list))

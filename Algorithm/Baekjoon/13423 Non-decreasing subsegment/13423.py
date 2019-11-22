# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

n = int(r_input())      # The size of list

num_list = list(map(int, r_input().split()))

max_cnt = 0
result = 0

cnt = 1
total = num_list[0]

for i in range(1, n):
    if num_list[i] < num_list[i-1]:
        if cnt > max_cnt:
            max_cnt = cnt
            result = total

        cnt = 1
        total = num_list[i]

    else:
        cnt += 1
        total += num_list[i]

if cnt > max_cnt:
    max_cnt = cnt
    result = total

print(max_cnt, result)

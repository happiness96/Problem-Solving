# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 수의 개수
nums = {}

for i in range(N):
    num = int(r_input())

    if num in nums:
        nums[num] += 1

    else:
        nums[num] = 1

for n in sorted(nums):
    print('\n'.join([str(n)]*nums[n]))

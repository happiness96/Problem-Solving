# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 수열 A의 크기
amount = [0] * 1001

result = 0

for num in map(int, r_input().split()):
    chk = 1

    for i in range(num-1, 0, -1):
        if amount[i] != 0:
            chk = 0
            amount[num] = max(amount[num], amount[i] + num)

    if chk:
        amount[num] = num

    result = max(result, amount[num])

print(result)

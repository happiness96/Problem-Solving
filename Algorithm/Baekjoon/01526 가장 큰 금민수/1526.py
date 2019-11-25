# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())

for i in range(N, -1, -1):
    num = str(i)
    flag = 0

    for c in num:
        if c not in '47':
            flag = 1
            break

    if flag:
        continue

    else:
        print(num)
        break

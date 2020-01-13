# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())
minimum = -1

for i in range(5000):
    if 3 * i > N:
        break

    tmp = N - 3 * i

    if tmp % 5 == 0:
        total = tmp // 5 + i

        if minimum < 0:
            minimum = total

        else:
            minimum = min(total, minimum)

print(minimum)

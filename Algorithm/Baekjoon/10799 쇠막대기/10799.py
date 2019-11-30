# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

bracket = r_input().rstrip()        # 괄호

total = 0

sticks = -1

for i in range(len(bracket)):
    if bracket[i] == '(':
        sticks += 1

    else:
        total += 1 if bracket[i - 1] == ')' else sticks
        sticks -= 1

print(total)

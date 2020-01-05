# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 명령의 수
N = int(r_input())
stack = []

for _ in range(N):
    order = r_input().rstrip()

    if order == 'top':
        print(stack[-1] if stack else -1)

    elif order == 'empty':
        print(0 if stack else 1)

    elif order == 'size':
        print(len(stack))

    elif order == 'pop':
        print(stack.pop() if stack else -1)

    else:
        X = int(order[5:])
        stack.append(X)

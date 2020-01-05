# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 피연산자의 개수
N = int(r_input())
postfix = r_input().rstrip()
stack = []

save = [int(r_input()) for _ in range(N)]

for component in postfix:
    if component == '+':
        stack.append(stack.pop() + stack.pop())

    elif component == '-':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2 - num1)

    elif component == '*':
        stack.append(stack.pop() * stack.pop())

    elif component == '/':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num2 / num1)

    else:
        stack.append(save[ord(component) - 65])

print('%.2f' % stack[0])

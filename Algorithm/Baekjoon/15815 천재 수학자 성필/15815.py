#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

expression = r().rstrip()       # 수식
stack = []              # 스택

for i in range(len(expression)):
    temp = expression[i]
    if temp == '*':
        stack.append(stack.pop() * stack.pop())
        
    elif temp == '/':
        b, a = stack.pop(), stack.pop()
        stack.append(a // b)
        
    elif temp == '+':
        stack.append(stack.pop() + stack.pop())
    
    elif temp == '-':
        b, a = stack.pop(), stack.pop()
        stack.append(a - b)
    
    else:
        stack.append(int(temp))

print(stack[0])

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 테스트 케이스의 개수
T = int(r_input())

for _ in range(T):
    stack = []
    flag = 0

    for parenthesis in r_input().rstrip():
        if parenthesis == '(':
            stack.append(1)
        else:
            if not stack:
                flag = 1
                break
            else:
                stack.pop()

    if stack:
        flag = 1

    print('NO' if flag else 'YES')

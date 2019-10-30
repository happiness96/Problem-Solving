#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

stack = []
N = int(r())
stack.append(N)

cnt = 1     # 연산 횟수

if N == 1:
    print(0)
    exit()

while 1:
    temp = []
    for num in stack:
        if num % 3 == 0:
            p = num // 3
            if p == 1:
                print(cnt)
                exit()
            temp.append(p)
            
        if num % 2 == 0:
            p = num // 2
            if p == 1:
                print(cnt)
                exit()
            temp.append(p)
            
        if num - 1 == 1:
            print(cnt)
            exit()
        temp.append(num - 1)
    
    cnt += 1
    stack = temp

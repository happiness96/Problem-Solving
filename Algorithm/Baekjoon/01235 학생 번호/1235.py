# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 학생의 수
students = []               # 학생들의 번호

for i in range(N):
    students.append(r_input().rstrip())

length = len(students[0])

for i in range(1, length+1):
    stack = []
    flag = 1

    for j in students:
        tmp = j[length - i:]
        if tmp in stack:
            flag = 0
            break
        stack.append(tmp)

    if flag:
        print(i)
        break

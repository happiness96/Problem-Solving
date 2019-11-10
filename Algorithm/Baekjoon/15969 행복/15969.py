# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 학생의 수

students = sorted(map(int, r_input().split()))

print(students[-1] - students[0])

# -*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N, X = map(int, r().split())        # N: 문자열의 길이, X: 문자열의 가치

if 26 * N < X or X < N:          # 조건을 만족하는 문자열이 존재하지 않으면
    print('!')
    exit()

X -= N

z = X // 25      # z의 개수
other = X % 25

if other:
    print('A' * (N - z - 1) + chr(65 + other) + 'Z' * z)

else:
    print('A' * (N - z) + 'Z' * z)

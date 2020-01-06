# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 테스트 케이스의 개수
T = int(r_input())
a, b = 0, 1
fibo = {0: 0, 1: 1}

for i in range(2, 100001):
    a, b = b, a + b
    fibo[b] = i

for _ in range(T):
    n = int(r_input())
    print(fibo[n])

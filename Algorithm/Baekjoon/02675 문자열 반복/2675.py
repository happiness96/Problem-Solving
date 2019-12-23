# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 테스트 케이스의 개수
T = int(r_input())

for _ in range(T):
    R, S = map(str, r_input().rstrip().split())

    for c in S:
        print(c * int(R), end='')

    print()

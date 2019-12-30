# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 테스트 케이스의 개수
T = int(r_input())

for _ in range(T):
    total = 0
    score = 0

    for c in r_input().rstrip():
        if c == 'O':
            score += 1
            total += score

        else:
            score = 0

    print(total)

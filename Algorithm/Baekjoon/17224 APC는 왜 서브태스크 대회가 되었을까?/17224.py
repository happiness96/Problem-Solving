# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# M: 문제의 수, L: 현정이의 역량, K: 현정이가 풀 수 있는 문제의 최대 개수
N, L, K = map(int, r_input().split())
hard = 0            # 현정이가 풀 수 있는 어려운 문제의 개수
easy = 0            # 현정이가 풀 수 있는 쉬운 문제의 개수

for i in range(N):
    sub1, sub2 = map(int, r_input().split())

    if sub2 <= L:
        hard += 1

    elif sub1 <= L:
        easy += 1

total = 0           # 점수 계산
if K < hard:
    total = K * 140
else:
    K -= hard
    total += hard * 140
    total += 100 * min(K, easy)

print(total)

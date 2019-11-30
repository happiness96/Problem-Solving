# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 온도를 측정한 전체 날짜 수, K:연속적인 날짜의 수
N, K = map(int, r_input().split())

temp = list(map(int, r_input().split()))

total = sum(temp[:K])
result = total

for i in range(N - K):
    total += temp[K + i] - temp[i]

    if total > result:
        result = total

print(result)

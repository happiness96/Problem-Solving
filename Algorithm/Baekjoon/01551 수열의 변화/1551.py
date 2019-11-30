# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, K = map(int, r_input().split())

sequence = list(map(int, r_input().split(',')))

for i in range(K):
    B = []
    for j in range(1, N - i):
        B.append(sequence[j] - sequence[j - 1])

    sequence = B

for i in range(len(sequence)):
    sequence[i] = str(sequence[i])

print(','.join(sequence))

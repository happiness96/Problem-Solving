# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

P = int(r_input())          # The number of data set

for _ in range(P):
    K, N = map(int, r_input().split())          # K: data set number

    S1 = (N * (1 + N)) // 2
    S2 = (N * (2 * N) // 2)
    S3 = (((2 * N) * (1 + N)) // 2)

    print(K, S1, S2, S3)

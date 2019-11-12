# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

A, B = map(str, r_input().rstrip().split())
result = 50

for i in range(len(B) - len(A) + 1):    # A 문자열의 비교 시작 인덱스
    cnt = 0     # A와 B의 차이

    for j in range(len(A)):
        if A[j] != B[i + j]:
            cnt += 1

    result = min(cnt, result)

print(result)

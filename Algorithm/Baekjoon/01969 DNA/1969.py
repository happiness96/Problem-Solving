# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())          # N: DNA의 수, M: 문자열의 길이
Hamming = []
result = ''

for _ in range(M):
    Hamming.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

for i in range(N):
    DNA = r_input().rstrip()

    for j in range(M):
        Hamming[j][DNA[j]] += 1

distance = 0        # Hamming distance
for i in range(M):
    temp = Hamming[i]
    m_cnt = 0
    output = ''

    for c in 'ACGT':
        if temp[c] > m_cnt:
            output = c
            m_cnt = temp[c]

    for c in 'ACGT':
        if c != output:
            distance += temp[c]

    result += output

print(result)
print(distance)

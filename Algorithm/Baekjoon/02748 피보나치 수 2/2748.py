# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

fibonacci = [0, 1]

for _ in range(2, 91):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

n = int(r_input())
print(fibonacci[n])

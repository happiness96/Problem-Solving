# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

NR, NC = map(int, r_input().split())

milk = []

for _ in range(NR):
    milk.append(list(map(int, r_input().split())))

result_sum = 0
result_r, result_c = 0, 0

for r in range(NR-2):
    for c in range(NC - 2):
        total = 0
        for i in range(3):
            total += sum(milk[r + i][c:c+3])

        if total > result_sum:
            result_sum = total
            result_r, result_c = r, c

print(result_sum)
print(result_r + 1, result_c + 1)

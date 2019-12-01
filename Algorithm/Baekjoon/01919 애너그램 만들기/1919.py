# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

s1 = r_input().rstrip()
s2 = r_input().rstrip()

cons_1 = [0] * 26
cons_2 = [0] * 26


for c in s1:
    cons_1[ord(c) - 97] += 1

for c in s2:
    cons_2[ord(c) - 97] += 1

result = 0
for i in range(26):
    result += abs(cons_1[i] - cons_2[i])

print(result)

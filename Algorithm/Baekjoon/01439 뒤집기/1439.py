# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 문자열 S
S = r_input().rstrip()

save = [0, 0]

save[int(S[0])] += 1

for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        save[int(S[i])] += 1

print(min(save))

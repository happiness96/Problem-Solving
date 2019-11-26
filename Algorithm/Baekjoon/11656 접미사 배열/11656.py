# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

S = r_input().rstrip()
suffix = []             # 접미사 배열

for i in range(len(S)):
    suffix.append(S[i:])

for c in sorted(suffix):
    print(c)

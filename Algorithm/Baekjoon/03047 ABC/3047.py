# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

abc_list = sorted(map(int, r_input().split()))
S = r_input().rstrip()

for c in S:
    print(abc_list[ord(c) - 65], end=' ')

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = sorted(r_input().rstrip(), reverse=True)

print(''.join(N))

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

M, N = map(int, r_input().split())      # M줄 N칸
result = 2 * (min(M, N)-1)

print(result if M <= N else result + 1)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

n = int(r_input())          # n: 물건의 총 개수

s = r_input().rstrip()
print(s.count('pPAp'))

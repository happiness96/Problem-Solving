# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

L = int(r_input())
A = int(r_input())
B = int(r_input())
C = int(r_input())
D = int(r_input())

tmp1 = A//C
if A % C:
    tmp1 += 1

tmp2 = B//D
if B % D:
    tmp2 += 1

print(L - max(tmp1, tmp2))

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 문자열의 길이
L = int(r_input())
string = r_input().rstrip()
result = 0

for i, ch in enumerate(string):
    result += (ord(ch) - 96) * 31 ** i

print(result % 1234567891)

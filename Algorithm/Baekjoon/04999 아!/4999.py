# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

str1 = r_input().rstrip()
str2 = r_input().rstrip()

print('no' if len(str1) < len(str2) else 'go')

#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

s = r().rstrip()

l = len(s)

is_odd = 1

for i in range(l-1):
    for j in range(i+2, l):
        sub_s = s[i:j]
        if sub_s == sub_s[::-1]:        # 만약 팰린드롬 부분 문자열이라면
            if len(sub_s)%2 == 0:       # 부분 문자열의 길이가 짝수라면
                is_odd = 0

print('Odd.'if is_odd else 'Or not.')

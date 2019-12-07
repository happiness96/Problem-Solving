# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

result = ''
length = 0

while True:
    tmp = ''
    for c in r_input().rstrip():
        if c == '-' or 'A' <= c <= 'Z' or 'a' <= c <= 'z':
            tmp += c

        else:
            if tmp:
                if len(tmp) > length:
                    length = len(tmp)
                    result = tmp
                tmp = ''

    if tmp == 'E-N-D':
        break

    if tmp:
        if len(tmp) > length:
            length = len(tmp)
            result = tmp

print(result.lower())

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

s = r_input().rstrip()
blank = 0

chk = 0

for c in s:
    if c == '{':
        print(' '*(2 * blank) + '{')
        blank += 1
        chk = 0

    elif c == '}':
        blank -= 1
        if chk:
            print()
        print(' '*(2 * blank) + '}', end='')
        chk = 1

    elif c == ',':
        if chk:
            print(',')
        else:
            print(' '*(2 * blank) + ',')
        chk = 0

    else:
        if chk:
            print(c, end='')
        else:
            print(' '*(2 * blank) + c, end='')
            chk = 1

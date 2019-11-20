# -*- encoding: utf-8 -*-
import sys

for s in sys.stdin:
    s = s[:-1]
    while 'BUG' in s:
        s = s.replace('BUG', '')

    print(s)

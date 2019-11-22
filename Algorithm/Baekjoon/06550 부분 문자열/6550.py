# -*- encoding: utf-8 -*-
import sys

for string in sys.stdin:
    s, t = map(str, string.rstrip().split())

    flag = 0

    length = len(s)

    ind = 0

    for c in t:
        if s[ind] == c:
            ind += 1

        if ind == length:
            flag = 1
            break

    print('Yes' if flag else 'No')

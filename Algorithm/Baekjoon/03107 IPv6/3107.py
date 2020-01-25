# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

if __name__ == '__main__':
    s = r_input().rstrip()

    if s.startswith('::'):
        s = s[1:]

    if s.endswith('::'):
        s = s[:-1]

    ip_add = list(map(str, s.split(':')))
    length = len(ip_add)

    result = ''

    for i in range(length):
        if ip_add[i] == '':
            for _ in range(9 - length):
                result += '0000:'

        else:
            result += '0' * (4 - len(ip_add[i])) + ip_add[i] + ':'

    print(result[:-1])

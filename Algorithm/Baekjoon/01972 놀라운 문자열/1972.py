# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

while True:
    string = r_input().rstrip()

    if string == '*':
        break

    dup = 0

    for i in range(1, len(string)):
        stack = []

        for start in range(len(string) - i):
            tmp = string[start] + string[start + i]

            if tmp in stack:
                dup = 1
                break

            stack.append(tmp)

        if dup:
            break

    print(string, 'is', end=' ')

    if dup:
        print('NOT', end=' ')

    print('surprising.')

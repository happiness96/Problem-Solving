# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

if __name__ == '__main__':
    val = r_input().rstrip()

    if val[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or '__' in val:
        print('Error!')
        sys.exit()

    if '_' in val:
        flag = 0

        if val.startswith('_') or val.endswith('_'):
            print('Error!')
            sys.exit()

        for ban in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if ban in val:
                print('Error!')
                sys.exit()

        for c in val:
            if c == '_':
                flag = 1

            elif flag:
                print(c.upper(), end='')
                flag = 0

            else:
                print(c, end='')

    else:
        for c in val:
            if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print('_' + c.lower(), end='')

            else:
                print(c, end='')

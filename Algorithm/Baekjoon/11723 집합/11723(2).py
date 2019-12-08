# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

M = int(r_input())          # 연산의 개수
sss = [0] * 21

for _ in range(M):
    order = r_input().rstrip()

    if order == 'all':
        sss = [1] * 21

    elif order == 'empty':
        sss = [0] * 21

    else:
        o, x = map(str, order.split())
        x = int(x)

        if o == 'check':
            print(sss[x])

        elif o == 'add':
            sss[x] = 1

        elif o == 'remove':
            sss[x] = 0

        else:
            sss[x] = 0 if sss[x] else 1

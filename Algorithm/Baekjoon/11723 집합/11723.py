# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

M = int(r_input())          # 연산의 개수
sss = set()

for _ in range(M):
    order = r_input().rstrip()

    if order == 'all':
        sss = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}

    elif order == 'empty':
        sss.clear()

    else:
        o, x = map(str, order.split())

        if o == 'check':
            print(1 if x in sss else 0)

        elif o == 'add':
            sss.add(x)

        elif o == 'remove':
            if x in sss:
                sss.remove(x)

        else:
            if x in sss:
                sss.remove(x)
            else:
                sss.add(x)

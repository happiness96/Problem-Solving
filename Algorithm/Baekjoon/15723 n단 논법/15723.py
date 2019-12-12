# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

n = int(r_input())
save = {}

for _ in range(n):
    a, b = map(str, r_input().rstrip().split(' is '))

    if a in save:
        save[a].append(b)

    else:
        save[a] = [b]

m = int(r_input())

for _ in range(m):
    a, b = map(str, r_input().rstrip().split(' is '))

    flag = 1

    while True:
        if a == b:
            break

        if a not in save or len(save[a]) != 1:
            flag = 0
            break

        a = save[a][0]

    print('T' if flag else 'F')

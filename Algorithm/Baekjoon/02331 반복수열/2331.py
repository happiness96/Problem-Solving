# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

A, P = map(int, r_input().split())

num_list = [str(A)]

while True:
    tmp = 0

    for c in num_list[-1]:
        tmp += int(c) ** P

    tmp = str(tmp)

    if tmp in num_list:
        print(num_list.index(tmp))
        break

    num_list.append(tmp)

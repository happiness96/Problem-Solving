# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

n1 = int(r_input())
n2 = int(r_input())

tmp = n2 - n1

if tmp == 180 or tmp == -180:
    print(180)
    exit()

if n2 >= n1:
    if tmp < 180:
        print(tmp)
    else:
        print(-360 + tmp)
else:
    if tmp > -180:
        print(tmp)
    else:
        print(360 + tmp)

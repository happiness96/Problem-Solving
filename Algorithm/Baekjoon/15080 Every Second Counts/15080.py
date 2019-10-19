#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

h1, m1, s1 = map(int,r().split(' : '))
h2, m2, s2 = map(int,r().split(' : '))

h, m, s = h2 - h1, m2 - m1, s2 - s1

if s < 0:
    s += 60
    m -= 1

if m < 0:
    m += 60
    h -= 1

if h < 0:
    h += 24

print(h * 3600 + m * 60 + s)

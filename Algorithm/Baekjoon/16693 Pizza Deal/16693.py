#-*- encoding: utf-8 -*-
import sys
from math import pi
r=sys.stdin.readline

A1, P1 = map(int,r().split())       # A1: Slice pizza area, P1: Slice pizza price
R1, P2 = map(int,r().split())       # R1: Circular pizza radius, P2: Circular pizza price

A2 = R1 ** 2 * pi       # A2: Circular pizza area

print('Slice of pizza' if A1/P1 > A2/P2 else 'Whole pizza')

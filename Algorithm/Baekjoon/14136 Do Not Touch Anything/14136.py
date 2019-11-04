# -*- encoding: utf-8 -*-
import sys
import math
r = sys.stdin.readline

R, C, N = map(int, r().split())

temp1 = math.ceil(R/N)
temp2 = math.ceil(C/N)

print(temp1 * temp2)

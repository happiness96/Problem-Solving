# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # The number of spotted mosquito

x = []
y = []

for i in range(N):
    a, b = map(int, r_input().split())
    x.append(a)
    y.append(b)

garo = max(x) - min(x)
sero = max(y) - min(y)

print(max(garo, sero) ** 2)

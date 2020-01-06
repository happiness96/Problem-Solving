# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

a, b = 0, 1

n = int(r_input())

for i in range(abs(n) - 1):
    a, b = b, a + b
    a %= 1000000000
    b %= 1000000000

if n == 0:
    print(0)

elif n > 0:
    print(1)

else:
    print(1 if n % 2 else -1)

print(b if n else a)

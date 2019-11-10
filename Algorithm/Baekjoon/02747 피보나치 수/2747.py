# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

n = int(r_input())


def fibo(num1, num2):
    global n
    num1, num2 = num2, num1 + num2

    if n == 1:
        print(num2)

    else:
        n -= 1
        fibo(num1, num2)


if n == 0:
    print(0)

elif n == 1:
    print(1)

else:
    n -= 1
    fibo(0, 1)

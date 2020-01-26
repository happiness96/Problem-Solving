# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    n = int(r_input())

    a, b = 1, 2

    if n == 1:
        print(a)
        exit()

    for _ in range(n - 2):
        a, b = b, (a + b) % 10007

    print(b)


if __name__ == '__main__':
    run()

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    N, M = map(int, r_input().split())

    array = [1] * (M + 1)

    for i in range(2, M + 1):
        if array[i]:
            if i >= N:
                print(i)
            mult = 2

            while i * mult <= M:
                array[i * mult] = 0
                mult += 1


if __name__ == '__main__':
    run()

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    N, M = map(int, r_input().split())

    array = [0] + list(map(int, r_input().split()))

    for i in range(2, N + 1):
        array[i] += array[i - 1]

    for _ in range(M):
        i, j = map(int, r_input().split())

        print(array[j] - array[i - 1])


if __name__ == '__main__':
    run()

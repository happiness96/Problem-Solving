# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    result = [0] * 1001

    dial = [1] * 10

    for i in range(1, 1001):
        result[i] = sum(dial) % 1234567

        new_dial = [dial[1] + dial[3], dial[0] + dial[2] + dial[4], dial[1] + dial[5], dial[0] + dial[4] + dial[6],
                    dial[1] + dial[3] + dial[5] + dial[7], dial[2] + dial[4] + dial[8], dial[3] + dial[7] + dial[9],
                    dial[4] + dial[6] + dial[8], dial[5] + dial[7], dial[6]]

        dial = new_dial

    T = int(r_input())

    for _ in range(T):
        N = int(r_input())
        print(result[N])


if __name__ == '__main__':
    run()

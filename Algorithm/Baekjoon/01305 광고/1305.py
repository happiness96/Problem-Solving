# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

L = int(r_input())
string = r_input().rstrip()
pi = [0] * L


def make_pi_list():
    global result
    i = 0
    j = 1

    while j < L:
        if string[i] == string[j]:
            i += 1
            pi[j] = i
            j += 1

        elif i == 0:
            pi[j] = 0
            j += 1

        else:
            i = pi[i - 1]


make_pi_list()

print(L - pi[-1])

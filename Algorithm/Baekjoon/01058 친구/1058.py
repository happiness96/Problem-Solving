# -*- encoding: utf-8 -*-
import sys
from copy import deepcopy
r_input = sys.stdin.readline


def floyd():
    tmp_relationship = deepcopy(relationship)

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if relationship[j][i] and relationship[i][k]:
                    tmp_relationship[j][k] = 1

    result = 0

    for friends in tmp_relationship:
        total = sum(friends)

        if total > result:
            result = total

    print(max(0, result - 1))


N = int(r_input())
relationship = [[0] * N for _ in range(N)]

for i in range(N):
    s = r_input().rstrip()

    for j in range(N):
        if s[j] == 'Y':
            relationship[i][j] = 1

floyd()

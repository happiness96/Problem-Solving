# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 유저의 수, M: 친구 관계의 수
N, M = map(int, r_input().split())
INF = sys.maxsize
friend = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, r_input().split())
    friend[A][B] = 1
    friend[B][A] = 1


def floyd():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                tmp = friend[j][i] + friend[i][k]

                if tmp < friend[j][k]:
                    friend[j][k] = tmp


floyd()
min_value = sys.maxsize
min_index = 0

for i in range(1, N + 1):
    total = sum(friend[i][1:]) - 2

    if total < min_value:
        min_value = total
        min_index = i

print(min_index)

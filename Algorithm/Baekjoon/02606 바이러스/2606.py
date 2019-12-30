# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 컴퓨터의 수
N = int(r_input())
# C: 네트워크 상에 직접 연결되어 있는 컴퓨터 쌍의 수
C = int(r_input())

connect = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(C):
    a, b = map(int, r_input().split())
    connect[a][b] = 1
    connect[b][a] = 1


def floyd():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if connect[j][i] and connect[i][k]:
                    connect[j][k] = 1


floyd()
print(connect[1].count(1) - 1)

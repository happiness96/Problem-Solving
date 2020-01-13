# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def floyd():
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if G[j][i] and G[i][k]:
                    G[j][k] = 1


if __name__ == '__main__':
    N = int(r_input())
    G = [list(map(int, r_input().split())) for _ in range(N)]
    floyd()

    for g in G:
        print(*g)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 지도의 크기
M, N = map(int, r_input().split())
K = int(r_input())      # 조사 영역의 개수

jungle = [[0] * (N + 1) for _ in range(M + 1)]
sea = [[0] * (N + 1) for _ in range(M + 1)]
ice = [[0] * (N + 1) for _ in range(M + 1)]


def setting():
    for i in range(1, M + 1):
        for j, c in enumerate('0' + r_input().rstrip()):
            if j:
                jungle[i][j] = jungle[i - 1][j] + jungle[i][j - 1] - jungle[i - 1][j - 1]
                sea[i][j] = sea[i - 1][j] + sea[i][j - 1] - sea[i - 1][j - 1]
                ice[i][j] = ice[i - 1][j] + ice[i][j - 1] - ice[i - 1][j - 1]

                if c == 'J':
                    jungle[i][j] += 1
                elif c == 'O':
                    sea[i][j] += 1
                elif c == 'I':
                    ice[i][j] += 1


def printing():
    for _ in range(K):
        a, b, c, d = map(int, r_input().split())
        print(jungle[c][d] - jungle[c][b - 1] - jungle[a - 1][d] + jungle[a - 1][b - 1], end=' ')
        print(sea[c][d] - sea[c][b - 1] - sea[a - 1][d] + sea[a - 1][b - 1], end=' ')
        print(ice[c][d] - ice[c][b - 1] - ice[a - 1][d] + ice[a - 1][b - 1])


setting()
printing()

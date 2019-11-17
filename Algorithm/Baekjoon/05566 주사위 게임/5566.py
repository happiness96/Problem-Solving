# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())      # N:보드 게임의 칸 수, M: 상근이가 주사위를 던진 횟수
board = [0] * N             # 보드 각 칸의 지시 사항
loc = 0                     # 현재 위치

for i in range(N):
    board[i] = int(r_input())

for i in range(M):
    num = int(r_input())
    loc += num
    loc = min(loc, N-1)
    loc += board[loc]

    if loc >= N-1:
        print(i+1)
        break

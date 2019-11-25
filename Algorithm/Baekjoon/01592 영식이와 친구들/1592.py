# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 한 사람이 공을 M번 받았으면 게임이 끝난다.
N, M, L = map(int, r_input().split())

count = [0] * N         # 공을 받은 횟수

ball = 0

while True:
    count[ball] += 1

    if count[ball] == M:
        print(sum(count) - 1)
        break

    if count[ball] % 2:         # 현재 공을 받은 횟수가 홀수라면
        ball += L

        if ball >= N:
            ball -= N

    else:                       # 짝수라면
        ball -= L

        if ball < 0:
            ball += N

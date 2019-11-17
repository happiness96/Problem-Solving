# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

M = int(r_input())          # 컵의 위치를 바꾼 횟수
ball = 1                # 제일 처음 공이 들어있는 컵

for i in range(M):
    X, Y = map(int, r_input().split())          # X, Y의 위치를 바꾼다.

    if X == ball:
        ball = Y

    elif Y == ball:
        ball = X

print(ball)

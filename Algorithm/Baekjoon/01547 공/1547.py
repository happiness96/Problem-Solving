# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

M = int(r_input())          # 컵의 위치를 바꾼 횟수
ball = [0, 1, 0, 0]                # 제일 처음 공이 들어있는 컵

for i in range(M):
    X, Y = map(int, r_input().split())          # X, Y의 위치를 바꾼다.

    ball[X], ball[Y] = ball[Y], ball[X]

print(ball.index(1))

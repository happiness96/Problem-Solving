# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 신호등의 개수, L: 도로의 길이
N, L = list(map(int, r_input().split()))
loc = 0     # 현재 위치
time = 0    # 걸린 시간


def light(t, red, green):            # 현재 시간에 신호등이 빨간 불인지 초록 불인지 체크 후 시간 추가
    t %= (red + green)

    return red - t if t < red else 0


for _ in range(N):
    # D: 신호등의 위치, R: 빨간 불이 지속되는 시간, G: 초록 불이 지속되는 시간
    D, R, G = map(int, r_input().split())

    time += D - loc
    time += light(time, R, G)
    loc = D

time += L - loc     # 마지막 지점까지

print(time)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

T = int(r_input())          # 테스트 케이스의 개수

for i in range(T):
    # H: 호텔의 층 수, W: 각 층의 방 수, N: 몇 번째 손님
    H, W, N = map(int, r_input().split())

    floor = N % H       # 층 수
    number = N // H + 1     # 호 수

    if floor == 0:
        number -= 1
        floor = H

    print(floor * 100 + number)

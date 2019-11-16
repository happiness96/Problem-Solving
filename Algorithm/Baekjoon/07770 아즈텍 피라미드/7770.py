# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

blocks = 1                  # N층을 쌓았을 때 필요한 최소 블록의 수
height = 0                  # 가장 높은 안정적인 피라미드 높이
n = int(r_input())          # 사용할 수 있는 블록의 수
temp = 1

if n == 1:
    print(1)
    exit()

while True:
    blocks += 2 * temp + 2 * (height+1) + 1

    temp += 2 * (height + 1) + 1

    height += 1

    if n < blocks:
        break

print(height)

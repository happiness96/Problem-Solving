# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 새의 수

fly_to_the_sky = 1          # 하늘로 날아 올라가는 새의 수

second = 0                  # 총 소요된 시간

while N != 0:
    if N < fly_to_the_sky:
        fly_to_the_sky = 1

    N -= fly_to_the_sky
    second += 1
    fly_to_the_sky += 1

print(second)

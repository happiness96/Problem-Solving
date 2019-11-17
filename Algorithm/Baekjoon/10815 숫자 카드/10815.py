# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())      # 상근이가 가지고 있는 숫자 카드의 개수

cards = {}          # 상근이가 가지고 있는 카드

for num in map(int, r_input().split()):
    cards[num] = 1

M = int(r_input())          # 상근이가 가지고 있는지 구해야 할 정수의 개수

for num in map(int, r_input().split()):
    print(1 if num in cards else 0, end=' ')

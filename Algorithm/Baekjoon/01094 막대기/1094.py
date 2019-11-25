# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

X = int(r_input())          # 길이가 Xcm인 막대를 만들려고 한다.

sticks = [64]

while True:
    total = sum(sticks)         # 가지고 있는 막대들의 총합

    if total == X:
        print(len(sticks))
        break

    tmp = sticks.pop()
    sticks.append(tmp // 2)

    if sum(sticks) < X:
        sticks.append(tmp // 2)

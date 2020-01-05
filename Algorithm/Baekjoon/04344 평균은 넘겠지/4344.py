# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# 테스트 케이스의 개수
C = int(r_input())

for _ in range(C):
    save = deque(list(map(int, r_input().split())))
    N = save.popleft()

    avr = sum(save) / N

    over_avr = 0

    for score in save:
        if score > avr:
            over_avr += 1

    print('%.3f' % (over_avr / N * 100) + '%')

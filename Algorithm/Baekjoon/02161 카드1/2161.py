# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

N = int(r())            # 정수

cards = [i for i in range(1, N+1)]          # 카드들

while True:
    print(cards.pop(0), end=' ')            # 제일 밑에 있는 카드를 버린다.

    if len(cards) == 0:                     # 남은 카드가 없으면 끝
        break

    cards.append(cards.pop(0))              # 제일 밑에 있는 카드를 제일 위로 올린다.
    

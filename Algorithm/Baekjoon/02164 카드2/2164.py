# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# N 장의 카드가 있다.
N = int(r_input())

cards = deque(list(range(1, N + 1)))
last_card = 0

while cards:
    last_card = cards.popleft()

    if cards:
        cards.append(cards.popleft())

print(last_card)

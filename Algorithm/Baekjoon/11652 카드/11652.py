#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # 숫자 카드의 개수
cards = {}          # 각 숫자 카드의 개수 

how_many = 0        # 가장 많이 가지고 있는 카드의 개수
max_card_num = 0        # 가장 많이 가지고 있는 카드

for i in range(N):
    num = int(r())
    
    if not num in cards:
        cards[num] = 1
    else:
        cards[num] += 1
    
    if cards[num] >= how_many:
        if cards[num] > how_many:
            max_card_num = num
            how_many = cards[num]
        else:
            max_card_num = min(max_card_num, num)

print(max_card_num)

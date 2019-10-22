#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

while True:
    Cheryl = Tania = 0
    cards = r().rstrip()
    
    if cards == '#':
        break
    
    for i in map(str, cards.split()):
        if i == 'A':        # 1번 카드
            Cheryl += 1
        elif i == '*':      # 카드 리스트의 끝
            break
        else:
            card = int(i)
            if card % 2:        # 홀수일 경우
                Cheryl += 1
            else:               # 짝수일 경우
                Tania += 1
    
    print('Cheryl'if Cheryl > Tania else 'Tania' if Tania > Cheryl else 'Draw')

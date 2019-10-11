#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

while 1:
    n = int(r())            # n: The number of cards
    deck_of_cards = {}
    
    if n == 0:
        break
    
    for i in range(n):
        deck_of_cards[i] = r().rstrip()
        
    suffle_index = n//2         # 나눴을 때 뒷쪽 deck에서의 시작 인덱스 
    
    if n % 2:                   # 개수가 홀수로 나눠떨어지면 뒷쪽 시작 인덱스를 1 추가
        suffle_index += 1
        
    for i in range(n//2):
        print(deck_of_cards[i])
        print(deck_of_cards[suffle_index + i])
    
    if n % 2:
        print(deck_of_cards[suffle_index-1])

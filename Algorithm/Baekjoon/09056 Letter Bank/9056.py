#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # The number of case

for i in range(T):
    bank = {}
    
    first_word, second_word = map(str, r().rstrip().split())
    
    for c in first_word:        # first word를 bank에 저장
        bank[c] = 0
    
    yes_or_yes = 1
    
    for c in second_word:
        if not c in bank:       # 만약 bank에 저장되어있는 문자가 아니면 NO
            yes_or_yes = 0
            break
        bank[c] += 1
    
    for c in bank:
        if bank[c] == 0:              # bank의 문자 중 안쓴 문자가 있으면 NO
            yes_or_yes = 0
            break
    
    print("YES" if yes_or_yes else "NO")

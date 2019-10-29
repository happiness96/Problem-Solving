#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # T: 테스트 케이스의 개수

for i in range(T):
    L = r().rstrip()        # 강산이가 입력한 순서
    
    Left = {}       # 커서의 왼쪽
    Right = {}      # 커서의 오른쪽
    
    max_Left = 0
    max_Right = 0
    
    for c in range(len(L)):
        if L[c] == '-':
            if Left:
                Left.pop(max_Left)
                max_Left -= 1
            continue
        
        elif L[c] == '<':
            if Left:
                max_Right += 1
                Right[max_Right] = Left.pop(max_Left)
                max_Left -= 1
            continue
        
        elif L[c] == '>':
            if Right:
                max_Left += 1
                Left[max_Left] = Right.pop(max_Right)
                max_Right -= 1
            continue
        
        else:
            max_Left += 1
            Left[max_Left] = L[c]
    
    print(''.join(list(Left.values())) + ''.join(list(Right.values()))[::-1])

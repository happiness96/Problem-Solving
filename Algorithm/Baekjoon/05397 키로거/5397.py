#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # T: 테스트 케이스의 개수

for i in range(T):
    L = r().rstrip()        # 강산이가 입력한 순서
    
    Left = []       # 커서의 왼쪽
    Right = []      # 커서의 오른쪽
    
    for c in range(len(L)):
        if L[c] == '-':
            if Left:
                Left.pop()
            continue
        
        elif L[c] == '<':
            if Left:
                Right.append(Left.pop())
            continue
        
        elif L[c] == '>':
            if Right:
                Left.append(Right.pop())
            continue
        
        else:
            Left.append(L[c])
    
    print(''.join(Left) + ''.join(Right[::-1]))

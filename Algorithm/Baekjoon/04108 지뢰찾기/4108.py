#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

while 1:
    R, C = map(int, r().split())        # R: 행의 수, C: 열의 수
    
    if R == C == 0: break       # 0 0이 들어오면 종료
    
    mine = {}
    
    for i in range(R+2):        # 지뢰 개수 초기화
        mine[i] = [0] * (C+2)
    
    for i in range(1, R+1):
        line = '0' + r().rstrip()
        
        for j in range(1, C+1):             # 지뢰를 발견할 경우
            if line[j] == '*':
                mine[i][j] = '*'
                
                for k in range(i-1, i+2):           # 지뢰 근처에 지뢰가 없다면 + 1
                    for h in range(j-1, j+2):
                        if mine[k][h] != '*':
                            mine[k][h] += 1
    
    for i in range(1, R+1):
        for j in range(1, C+1):
            print(mine[i][j], end='')
        print()

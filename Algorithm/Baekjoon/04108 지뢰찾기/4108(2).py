#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

while 1:
    R, C = map(int, r().split())        # R: 행의 수, C: 열의 수
    
    if R == C == 0: break       # 0 0이 들어오면 종료
    
    mine = {0:[0]*(C+2), R+1:[0]*(C+2)}
    
    for i in range(1, R+1):        # 지뢰 밭 초기화
        mine[i] = [0]
        for j in r().rstrip():
            if j == '.':
                mine[i].append(0)
            else:
                mine[i].append(j)
        mine[i].append(0)
    
    for i in range(1, R+1):
        for j in range(1, C+1):
            if mine[i][j] != '*':           # 만약에 지뢰 자리가 아니라면
                for k in range(i-1, i+2):           # 주변 지뢰 탐색
                    for h in range(j-1, j+2):
                        if mine[k][h] == '*':
                            mine[i][j] += 1
    
    for i in range(1, R+1):
        for j in range(1, C+1):
            print(mine[i][j], end='')
        print()

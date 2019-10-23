#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # 테스트 케이스의 개수

for i in range(T):
    robots = {}         # 로봇들의 문자열
    N = int(r())        # 로봇의 개수
    
    for j in range(1, N+1):
        robots[j] = r().rstrip()

    k = len(robots[1])      # 라운드 수
    
    for j in range(k):
        status = {'R':[], 'S':[], 'P':[]}
        
        for robot in robots:
            status[robots[robot][j]].append(robot)
        
        t = len(robots)
        rock = len(status['R'])
        scissor = len(status['S'])
        paper = len(status['P'])
        
        if rock == t or scissor == t or paper == t:     # 모두 동일한걸 냈을 경우 다음 라운드로
            continue
        
        if rock == 0:       # 바위가 없을 경우
            for lose in status['P']:        # 보를 낸 로봇들을 탈락시킴
                robots.pop(lose)
            
        elif scissor == 0:  # 가위가 없을 경우
            for lose in status['R']:        # 묵을 낸 로봇들을 탈락시킴
                robots.pop(lose)
                
        elif paper == 0:    # 보가 없을 경우
            for lose in status['S']:        # 가위를 낸 로봇들을 탈락시킴
                robots.pop(lose)
    
    if len(robots) > 1:
        print(0)
        
    else:
        for result in robots:
            print(result)

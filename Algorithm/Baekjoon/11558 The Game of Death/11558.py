#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # T: The number of Test Case

for i in range(T):
    N = int(r())        # N: The number of Players
    
    the_game_of_death = {}
    
    for j in range(1, N+1):
        the_game_of_death[j] = int(r())
    
    node = 1
    visit = [1]
    
    while 1:
        node = the_game_of_death[node]
        
        if node == N:           # 주경이가 걸린다면
            print(len(visit))
            break
        
        if node in visit:       # 주경이가 절대 걸리지 않는다면
            print(0)
            break
        
        visit.append(node)

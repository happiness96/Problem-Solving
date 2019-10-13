#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # The number of consecutive dotation days

donation_pack = [0] * 3

for i in range(T):
    donation = list(map(int,r().split()))
    
    for j in range(3):
        donation_pack[j] += donation[j]
    
    dist = min(donation_pack)
    
    if dist < 30:
        print('NO')
    else:
        print(dist)
        
        for j in range(3):
            donation_pack[j] -= dist

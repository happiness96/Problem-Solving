#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # 테스트 케이스의 수

for i in range(T):
    N = int(r())        # 맛살의 종류
    eff = {}
    
    for matsal in range(N):
        W, C = map(int,r().split())
        t = W/C
        
        if t in eff:
            eff[t] = min(C, eff[t])
        else:
            eff[t] = C
            
    print(eff[max(eff)])

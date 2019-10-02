#-*- encoding: utf-8 -*-
import sys
while 1:
    try :
        T = sys.stdin.readline()[:-1]   # 테스트 케이스
        N,B,M = map(float,T.split())    # N: 초기 조금액     B: 이율    M: 목표 금액
        year = 1
        while 1:
            N+=N*B/100
            if N > M:break          # 목표 금액에 달성하면 break
            year+=1
        print(year)
    except:         # EOF break
        break

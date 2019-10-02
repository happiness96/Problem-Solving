#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # 테스트 케이스 개수

for N in map(int,r().split()):
    end1 = end2 = end3 = 0          # 3, 7, 21로 나누었을 때 마지막 항
    n1 = n2 = n3 = 0        # 항의 개수
    total = 0
    for i in range(3):
        if (N-i) % 3 == 0:
            end1 = N-i
            n1 = (N-i)//3
    total += (n1 * (3 + end1)) // 2       # 등차 수열 합
    
    for i in range(7):
        if (N-i) % 7 == 0:
            end2 = N-i
            n2 = (N-i)//7
    total += (n2 * (7 + end2)) // 2
    
    if N >= 21:
        for i in range(21):
            if (N-i) % 21 == 0:
                end3 = N-i
                n3 = (N-i)//21
        total -= (n3 * (21 + end3)) // 2
    print(total)

#-*- encoding: utf-8 -*-
import sys
from itertools import combinations
r=sys.stdin.readline

while 1:
    test_input = list(map(int, r().split()))
    if test_input == [0]:break
    
    k = test_input[0]       # 집합 S를 만드는 숫자의 개수
    S = test_input[1:]      # 집합 S
    
    for i in list(combinations(S, 6)):
        for c in i:
            print(c, end=' ')
        print()
    print()

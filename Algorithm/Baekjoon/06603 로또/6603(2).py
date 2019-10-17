#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline


def lotto(cnt, node, numbers):      # DFS 방식, lotto 번호를 추첨
    if cnt == 6:
        for num in numbers:
            print(num, end=' ')
        print()
        
    else:
        for i in range(node + 1, k):
            lotto(cnt + 1, i, numbers + [S[i]])
    
    
while 1:
    test_input = list(map(int, r().split()))
    if test_input == [0]:break
    
    k = test_input[0]       # 집합 S를 만드는 숫자의 개수
    S = test_input[1:]      # 집합 S

    for i in range(k-5):
        lotto(1, i, [S[i]])
        
    print()

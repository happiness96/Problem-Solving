#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

test_case = int(r())

for i in range(test_case):
    N, M = map(int,r().split())     # N: 문서의 수, M: 몇 번째로 인쇄되었는지 궁금한 문서의 현재 위치
    queue = list(map(int,r().split()))
    
    cnt = 0         # 몇 번째로 인쇄 되는지
    important = 9   # 중요도
    ind = 0         # 문서 탐색 인덱스
    
    while 1:
        while 1:
            if queue.count(important) == 0:     # 해당 중요도가 문서에 있는지 체크
                important -= 1
            else:
                break
        
        if queue[ind] == important:
            cnt += 1
            queue[ind] = 0
            
            if ind == M:
                break
        
        ind += 1
        
        if ind == N:        # 문서의 끝까지 탐색했으면 다시 처음부터 탐색
            ind = 0
        
    print(cnt)

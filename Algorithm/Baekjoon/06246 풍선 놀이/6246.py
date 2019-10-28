#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N, Q = map(int, r().split())        # N: 슬롯의 개수, Q: 풍선들을 꽂는 횟수
slot = [0] * N

for i in range(Q):
    L, I = map(int, r().split())        # 슬롯 L부터 I개씩 띄워서 풍선을 놓자.
    m = 0
    
    while 1:
        ind = L + I * m - 1
        if ind >= N:
            break
        slot[ind] = 1
        m += 1

print(slot.count(0))

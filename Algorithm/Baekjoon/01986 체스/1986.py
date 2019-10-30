#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

n, m = map(int, r().split())        # n행 x m열

chess = {}              # 체스판

for i in range(1, n+1):         # 0: 안전한 칸, 1: 안전하지 않은 칸
    chess[i] = [0] * (m + 1)


Q = list(map(int, r().split()))         # Queen
K = list(map(int, r().split()))         # Knight
P = list(map(int, r().split()))         # Pawn


for i in range(P[0]):               # 폰 두기
    r, c = P[2*i+1], P[2*i+2]
    chess[r][c] = 'P'


for i in range(K[0]):           # 나이트 두기
    r, c = K[2*i+1], K[2*i+2]
    chess[r][c] = 'K'
    
    if r-2 > 0:
        if c-1 > 0:
            if not chess[r-2][c-1] in ['P','K','Q']:
                chess[r-2][c-1] = 1
        if c+1 <= m:
            if not chess[r-2][c+1] in ['P','K','Q']:
                chess[r-2][c+1] = 1
                
    if r-1 > 0:
        if c-2 > 0:
            if not chess[r-1][c-2] in ['P','K','Q']:
                chess[r-1][c-2] = 1
        if c+2 <= m:
            if not chess[r-1][c+2] in ['P','K','Q']:
                chess[r-1][c+2] = 1
    
    if r+2 <= n:
        if c-1 > 0:
            if not chess[r+2][c-1] in ['P','K','Q']:
                chess[r+2][c-1] = 1
        if c+1 <= m:
            if not chess[r+2][c+1] in ['P','K','Q']:
                chess[r+2][c+1] = 1
    
    if r+1 <= n:
        if c-2 > 0:
            if not chess[r+1][c-2] in ['P','K','Q']:
                chess[r+1][c-2] = 1
        if c+2 <= m:
            if not chess[r+1][c+2] in ['P','K','Q']:
                chess[r+1][c+2] = 1


for i in range(Q[0]):       # Queen의 개수만큼 반복
    r, c = Q[2*i+1], Q[2*i+2]
    chess[r][c] = 'Q'
    
    temp_c = c-1            # Queen의 왼쪽
    while temp_c > 0:
        if chess[r][temp_c] in ['P','K','Q']:       # 장애물에 막히는 경우
            break
        else:
            chess[r][temp_c] = 1
        temp_c -= 1
    
    temp_c = c-1            # Queen의 왼쪽 위 대각선
    temp_r = r-1
    while temp_c > 0 and temp_r > 0:
        if chess[temp_r][temp_c] in ['P','K','Q']:
            break
        else:
            chess[temp_r][temp_c] = 1
        temp_c -= 1
        temp_r -= 1
    
    temp_c = c-1            # Queen의 왼쪽 아래 대각선
    temp_r = r+1
    while temp_c > 0 and temp_r <= n:
        if chess[temp_r][temp_c] in ['P','K','Q']:
            break
        else:
            chess[temp_r][temp_c] = 1
        temp_c -= 1
        temp_r += 1
    
    temp_r = r-1            # Queen의 위쪽
    while temp_r > 0:
        if chess[temp_r][c] in ['P','K','Q']:
            break
        else:
            chess[temp_r][c] = 1
        temp_r -= 1
    
    temp_r = r+1            # Queen의 아래쪽
    while temp_r <= n:
        if chess[temp_r][c] in ['P','K','Q']:
            break
        else:
            chess[temp_r][c] = 1
        temp_r += 1
    
    temp_c = c+1            # Queen의 오른쪽
    while temp_c <= m:
        if chess[r][temp_c] in ['P','K','Q']:
            break
        else:
            chess[r][temp_c] = 1
        temp_c += 1
    
    temp_r = r-1            # Queen의 오른쪽 위 대각선
    temp_c = c+1
    while temp_r > 0 and temp_c <= m:
        if chess[temp_r][temp_c] in ['P','K','Q']:
            break
        else:
            chess[temp_r][temp_c] = 1
        temp_r -= 1
        temp_c += 1
    
    temp_r = r+1            # Queen의 오른쪽 아래 대각선
    temp_c = c+1
    while temp_r <= n and temp_c <= m:
        if chess[temp_r][temp_c] in ['P','K','Q']:
            break
        else:
            chess[temp_r][temp_c] = 1
        temp_r += 1
        temp_c += 1

cnt = 0
for i in range(1, n+1):
    cnt += chess[i][1:m+1].count(0)
print(cnt)

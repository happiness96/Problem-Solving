#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

blank = {}      # 집
N = int(r())    # 집의 크기

for i in range(N):
    blank[i]=list(map(int,r().split()))
    
result = 0          # 결과 (방법의 개수)

def bfs(r1, c1, r2, c2):
    global result
    
    if r2 == c2 == N-1:     # 파이프 한쪽 끝이 (N,N)에 다다르면 result 1 증가
        result += 1
    else:
        if r2-r1 == c2-c1 == 1:         # 파이프가 대각선일 경우
            temp_r, temp_c = r2 + 1, c2
            if temp_r < N:
                if blank[temp_r][temp_c] == 0:
                    bfs(r2, c2, temp_r,temp_c)
                    
            temp_r, temp_c = r2 + 1, c2 + 1
            if temp_r < N and temp_c < N:
                if not 1 in [blank[temp_r][temp_c], blank[temp_r-1][temp_c], blank[temp_r][temp_c-1]]:
                    bfs(r2, c2, temp_r,temp_c)
            
            temp_r, temp_c = r2, c2 + 1
            if temp_c < N:
                if blank[temp_r][temp_c] == 0:
                    bfs(r2, c2, temp_r,temp_c)
        
        elif c2-c1 == 1:          # 파이프가 가로일 경우
            temp_r, temp_c = r2 + 1, c2 + 1
            if temp_r < N and temp_c < N:
                if not 1 in [blank[temp_r][temp_c], blank[temp_r-1][temp_c], blank[temp_r][temp_c-1]]:
                    bfs(r2, c2, temp_r,temp_c)
                    
            temp_r, temp_c = r2, c2 + 1
            if temp_c < N:
                if blank[temp_r][temp_c] == 0:
                    bfs(r2, c2, temp_r,temp_c)
        
        elif r2-r1 == 1:              # 파이프가 세로일 경우
            temp_r, temp_c = r2 + 1, c2
            if temp_r < N:
                if blank[temp_r][temp_c] == 0:
                    bfs(r2, c2, temp_r,temp_c)
                    
            temp_r, temp_c = r2 + 1, c2 + 1
            if temp_r < N and temp_c < N:
                if not 1 in [blank[temp_r][temp_c], blank[temp_r-1][temp_c], blank[temp_r][temp_c-1]]:
                    bfs(r2, c2, temp_r,temp_c)

bfs(0, 0, 0, 1)
print(result)

#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

R,C = map(int,r().split())      # 지도의 크기 R: 행, C: 열
maap = {0:['.']*(C+2), R+1:['.']*(C+2)}     # 현재 지도

for i in range(1, R+1):         # 지도의 사방에 바다를 추가적으로 확장 
    maap[i] = ['.']
    for c in r()[:-1]:
        maap[i].append(c)
    maap[i].append('.')

for i in range(1, R+1):         # 50년 후 잠길 섬 검사
    for j in range(1, C+1):
        if maap[i][j]=='X':
            temp = [maap[i][j-1], maap[i][j+1], maap[i-1][j], maap[i+1][j]]
            if temp.count('.') >= 3:    # 삼면이 바다면 잠긴다
                maap[i][j] = ','

for i in range(1, R+1):
    for j in range(1, C+1):
        if maap[i][j]==',':maap[i][j]='.'
        
R_start, R_end, C_start, C_end = 1, R, 1, C

# 결과에서
for i in range(1, R+1):         # 위쪽 면이 바다인 부분 처리 
    if not ''.join(maap[i][1:-1]) == '.' * C:
        R_start = i
        break

for i in range(R):              # 아래쪽이 바다인 부분 처리
    if not ''.join(maap[R-i][1:-1]) == '.' * C :
        R_end = R-i
        break

for i in range(1, R+1):         # 왼쪽, 오른쪽이 바다인 부분 처리
    for j in range(C_start,C+1):
        temp = ''
        for k in range(1, R+1):
            temp+=maap[k][j]
        if temp != '.' * R: C_start = j;break
        
    for j in range(C):
        temp = ''
        for k in range(1, R+1):
            temp+=maap[k][C-j]
        if temp != '.' * R: C_end = C-j;break
        
for i in range(R_start, R_end+1):
    print(''.join(maap[i][C_start : C_end+1]))

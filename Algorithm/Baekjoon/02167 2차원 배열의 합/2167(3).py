#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N,M = map(int,r().split())      # 배열의 크기 (N x M)

array_set = {0:[0]*(M+1), 1:[0]}                  # 1,1에서 N', M'까지의 누적 합을 저장할 배열

for i in map(int,r().split()):      # 첫 줄은 그냥 누적합을 넣는다.
        array_set[1].append(array_set[1][-1] + i)
        
for i in range(2, N+1):             # 두 번째 줄 부터는 1,1부터 해당 칸까지 누적 합을 계산하여 넣는다.
    array_set[i] = [0]
    row_list = [0] + list(map(int,r().split()))
    
    for j in range(1, M+1):
        array_set[i].append(row_list[j] + array_set[i][j-1] + array_set[i-1][j] - array_set[i-1][j-1])
    

K = int(r())        # 합을 구할 부분의 개수

for quest in range(K):
    i, j, x, y = map(int,r().split())       # i행 j열부터 x행 y열까지
    total = 0           # 합계
    
    total = array_set[x][y] - array_set[x][j-1] - array_set[i-1][y] + array_set[i-1][j-1]
    
    print(total)

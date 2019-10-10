#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N,M = map(int,r().split())      # 영토의 범위 (N x M)

population = {0:[0]*(M+1), 1:[0]}                  # 1,1에서 N', M'까지 살고있는 사람들의 누적 합을 저장할 배열

for i in map(int,r().split()):      # 첫 줄은 그냥 누적합을 넣는다.
        population[1].append(population[1][-1] + i)
        
for i in range(2, N+1):             # 두 번째 줄 부터는 1,1부터 해당 칸까지 누적 합을 계산하여 넣는다.
    population[i] = [0]
    row_list = [0] + list(map(int,r().split()))
    
    for j in range(1, M+1):
        population[i].append(row_list[j] + population[i][j-1] + population[i-1][j] - population[i-1][j-1])
    

K = int(r())        # 진경 대왕이 인구수를 궁금해하는 직사각형 범위 개수 

for quest in range(K):
    x1, y1, x2, y2 = map(int,r().split())       # x1, y1부터 x2, y2까지
    total = 0           # 사는 인구 수 합계
    
    total = population[x2][y2] - population[x2][y1-1] - population[x1-1][y2] + population[x1-1][y1-1]
    
    print(total)

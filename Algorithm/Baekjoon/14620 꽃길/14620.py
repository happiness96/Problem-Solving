# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 화단 한 변의 크기
flower = {}                 # 각 지점당 가격
flower_cost = {}            # 각 지점에 꽃을 심는 비용

for i in range(N):
    flower[i] = list(map(int, r_input().split()))
    flower_cost[i] = [14620] * N

for i in range(1, N-1):
    for j in range(1, N-1):
        flower_cost[i][j] = flower[i-1][j] + flower[i+1][j] + flower[i][j-1] + flower[i][j+1] + flower[i][j]


def min_cost(cnt, i, j, total):     # 세 씨앗을 심는 최소 비용 찾기(DFS)
    global cost, check
    temp1 = [[i, j], [i-1, j], [i+1, j], [i, j-1], [i, j+1]]        # (i, j)에 씨앗을 심으면 해당 범위 내는 방문 처리 해줘야 함

    for t in temp1:
        check[t[0]][t[1]] = 1

    total += flower_cost[i][j]

    if cnt == 3:                # 세 씨앗을 모두 심었으면
        cost = min(cost, total)

    else:
        for a in range(j + 2, N - 1):
            # 다음 심을 씨앗 근처에 심으면 안되는 구역이 있는지 체크
            temp2 = [check[i - 1][a], check[i + 1][a], check[i][a - 1], check[i][a + 1], check[i][a]]

            if not 1 in temp2:
                min_cost(cnt + 1, i, a, total)

        for a in range(i + 1, N - 1):
            for b in range(1, N - 1):
                temp2 = [check[a - 1][b], check[a + 1][b], check[a][b - 1], check[a][b + 1], check[a][b]]

                if not 1 in temp2:
                    min_cost(cnt + 1, a, b, total)

    for t in temp1:
        check[t[0]][t[1]] = 0


check = []          # 꽃 범위 체크

for i in range(N):
    check.append([0] * N)
    
cost = 14620        # 최소 비용

for i in range(1, N-1):
    for j in range(1, N-1):
        min_cost(1, i, j, 0)

print(cost)

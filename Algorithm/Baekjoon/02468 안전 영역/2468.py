# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(r_input())          # 2차원 배열의 행과 열의 개수
area = {}                   # 영역
result = 1                  # 안전한 영역의 최대 개수

search_list = []            # 탐색할 깊이

for i in range(N):
    s = list(map(int, r_input().split()))
    area[i] = s

    for c in s:
        if c not in search_list:
            search_list.append(c)


def count_area(temp_area, pre_search):           # 안전한 영역의 볌위 찾기
    next_search = []            # 다음 탐색할 좌표

    for loc in pre_search:
        temp = [[loc[0]-1, loc[1]], [loc[0]+1, loc[1]], [loc[0], loc[1]-1], [loc[0], loc[1]+1]]
        temp_area[loc[0]][loc[1]] = 0           # 이미 방문

        for i in range(4):
            if 0 <= temp[i][0] < N and 0 <= temp[i][1] < N:
                if temp_area[temp[i][0]][temp[i][1]]:
                    if [temp[i][0], temp[i][1]] not in next_search:
                        next_search.append([temp[i][0], temp[i][1]])

    if next_search:
        count_area(temp_area, next_search)


def cnt_area(height):          # 안전 영역 개수 찾기
    global result
    temp_area = {}          # 안전 영역
    cnt = 0                 # 안전 영역의 개수

    for i in range(N):              # 안전 영역 구하기
        temp_area[i] = []

        for j in range(N):
            temp_area[i].append(0 if area[i][j] <= height else 1)

    for i in range(N):
        for j in range(N):
            if temp_area[i][j] == 1:
                count_area(temp_area, [[i, j]])
                cnt += 1

    result = max(result, cnt)


for i in search_list:
    cnt_area(i)

print(result)

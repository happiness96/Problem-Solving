# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, r_input().split())                # 도화지의 세로, 가로 크기
# drawing = {0: [0]*(m+2), n+1: [0]*(m+2)}        # 그림
drawing = deque()
drawing_cnt = 0             # 그림의 개수
max_area = 0                # 가장 넓은 그림의 넓이
ad1 = [0, 0, 1, -1]
ad2 = [1, -1, 0, 0]

drawing.append([0]*(m+2))

for i in range(1, n+1):
    drawing.append([0] + list(map(int, r_input().split())) + [0])

drawing.append([0]*(m+2))


def find_picture(search, size):       # 그림 영역 찾기 (BFS)
    global max_area

    while search:
        loc = search.popleft()
        drawing[loc[0]][loc[1]] = 0
        size += 1

        for i in range(4):
            temp_row = loc[0] + ad1[i]
            temp_col = loc[1] + ad2[i]

            if drawing[temp_row][temp_col] == 1:
                drawing[temp_row][temp_col] = 0
                search.append([temp_row, temp_col])

    max_area = max(max_area, size)


for i in range(1, n+1):
    for j in range(1, m+1):
        if drawing[i][j] == 1:              # 그림을 찾았다면
            temp = deque()
            temp.append([i, j])
            drawing[i][j] = 0
            find_picture(temp, 0)
            drawing_cnt += 1

print(drawing_cnt)
print(max_area)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

M, N, K = map(int, r_input().split())     # M x N 인 모눈종이, K개의 직 사각형
rect = {}

for i in range(M):
    rect[i] = [1] * N

for _ in range(K):
    x1, y1, x2, y2 = map(int, r_input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            rect[y][x] = 0


def find_area(pre_visit, cnt):            # 영역 구하기
    next_visit = []

    while pre_visit:
        a = pre_visit.pop()

        temp = [[a[0]-1, a[1]], [a[0]+1, a[1]], [a[0], a[1]-1], [a[0], a[1]+1]]
        rect[a[0]][a[1]] = 0
        cnt += 1

        for b in temp:
            if 0 <= b[0] < M and 0 <= b[1] < N:
                if rect[b[0]][b[1]] == 1:
                    if [b[0], b[1]] not in next_visit:
                        next_visit.append([b[0], b[1]])

    if next_visit:
        find_area(next_visit, cnt)

    else:
        area.append(cnt)


area = []               # 영역의 크기

for i in range(M):
    for j in range(N):
        if rect[i][j] == 1:
            find_area([[i, j]], 0)

print(len(area))

for a in sorted(area):
    print(a, end=' ')

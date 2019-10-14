#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

n, m = map(int, r().split())        # n x m 행렬

row_nine = []       # 각 행의 9 개수
col_nine = []       # 각 열의 9 개수

bingo = {}          # 빙고판

for i in range(n):      # 각 행의 9의 개수를 row_nine에 저장
    row = r().rstrip()
    row_nine.append(row.count('9'))
    bingo[i] = list(row.split())

for i in range(m):      # 각 열의 9의 개수를 col_nine에 저장
    cnt_nine = 0
    for j in range(n):
        cnt_nine += bingo[j][i].count('9')
    col_nine.append(cnt_nine)

max_row = max(row_nine)
max_col = max(col_nine)

print(sum(row_nine) - max(max_row, max_col))

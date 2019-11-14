# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())      # N: 영상의 크기

media = []              # 영상 데이터 정보

for i in range(N):
    media.append(list(r_input().rstrip()))


def find_str(row, col, s_size):
    temp = ''

    for i in range(row, row + s_size):
        for j in range(col, col + s_size):
            temp += media[i][j]

    if temp == temp[0] * s_size ** 2:
        return temp[0]

    else:
        return -1


def compress(start_row, start_col, size):       # 영상 데이터 압축하기
    print('(', end='')

    tmp = size // 2

    chk = find_str(start_row, start_col, tmp)       # 왼쪽 위
    if chk == -1:
        compress(start_row, start_col, tmp)
    else:
        print(chk, end='')

    chk = find_str(start_row, start_col + tmp, tmp)         # 오른쪽 위
    if chk == -1:
        compress(start_row, start_col + tmp, tmp)
    else:
        print(chk, end='')

    chk = find_str(start_row + tmp, start_col, tmp)         # 왼쪽 아래
    if chk == -1:
        compress(start_row + tmp, start_col, tmp)
    else:
        print(chk, end='')

    chk = find_str(start_row + tmp, start_col + tmp, tmp)       # 오른쪽 아래
    if chk == -1:
        compress(start_row + tmp, start_col + tmp, tmp)
    else:
        print(chk, end='')

    print(')', end='')


# 초기 검사
s = find_str(0, 0, N)
if s != -1:
    print(s)
    exit()

compress(0, 0, N)

# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

n = int(r())            # 목판의 크기
moving = r().rstrip()           # 로봇의 움직임
current_r = 0
current_c = 0

wood = {}               # 목판

for i in range(n):
    wood[i] = ['.'] * n


def up_down(row, col):
    if wood[row][col] in '-+':
        wood[row][col] = '+'
    else:
        wood[row][col] = '|'


def left_right(row, col):
    if wood[row][col] in '|+':
        wood[row][col] = '+'
    else:
        wood[row][col] = '-'


for c in moving:
    if c == 'D':
        if current_r < n-1:
            up_down(current_r, current_c)
            current_r += 1
            up_down(current_r, current_c)

    elif c == 'U':
        if current_r > 0:
            up_down(current_r, current_c)
            current_r -= 1
            up_down(current_r, current_c)

    elif c == 'L':
        if current_c > 0:
            left_right(current_r, current_c)
            current_c -= 1
            left_right(current_r, current_c)

    else:
        if current_c < n-1:
            left_right(current_r, current_c)
            current_c += 1
            left_right(current_r, current_c)

for i in wood:
    print(''.join(wood[i]))

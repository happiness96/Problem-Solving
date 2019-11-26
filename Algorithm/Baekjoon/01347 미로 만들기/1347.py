# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

n = int(r_input())          # 홍준이가 적은 내용의 길이
S = r_input().rstrip()      # 그 내용

# 홍준이가 보고있는 방향 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
direction = 2

maze = deque()
maze.append(deque())
maze[0].append('.')

row, col = 0, 0         # 홍준이의 현재 위치

for order in S:
    if order == 'R':            # 오른쪽으로 전환
        direction += 1

        if direction == 4:
            direction = 0

    elif order == 'L':            # 왼쪽으로 전환
        direction -= 1

        if direction == -1:
            direction = 3

    else:                       # 앞으로 전진
        if direction == 0:      # 북쪽으로 보고있는 경우
            if row == 0:
                maze.appendleft(deque())
                for _ in range(len(maze[1])):
                    maze[0].append('#')
            else:
                row -= 1

        elif direction == 1:        # 동쪽으로 보고있는 경우
            col += 1
            if col == len(maze[0]):
                for a in maze:
                    a.append('#')

        elif direction == 2:        # 남쪽으로 보고있는 경우
            row += 1
            if row == len(maze):
                maze.append(deque())
                for _ in range(len(maze[0])):
                    maze[-1].append('#')

        else:                       # 서쪽으로 보고있는 경우
            if col == 0:
                for a in maze:
                    a.appendleft('#')
            else:
                col -= 1

        maze[row][col] = '.'

for c in maze:
    print(''.join(c))

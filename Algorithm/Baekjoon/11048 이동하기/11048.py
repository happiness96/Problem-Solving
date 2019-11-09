# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())          # 미로의 크기
maze = [0] * M

for i in range(N):                          # (DP)
    input_maze = list(map(int, r_input().split()))
    maze[0] += input_maze[0]

    for j in range(1, M):
        maze[j] = max(maze[j-1], maze[j]) + input_maze[j]

print(maze[-1])

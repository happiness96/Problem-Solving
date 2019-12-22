# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 미로의 크기
N = int(r_input())

# 미로
maze = list(map(int, r_input().split()))

jump_count = [sys.maxsize] * N

cnt = 0
jump_count[0] = cnt

for i in range(N):
    cnt = jump_count[i] + 1
    for j in range(i, min(i + maze[i] + 1, N)):
        jump_count[j] = min(jump_count[j], cnt)

print(-1 if jump_count[-1] == sys.maxsize else jump_count[-1])

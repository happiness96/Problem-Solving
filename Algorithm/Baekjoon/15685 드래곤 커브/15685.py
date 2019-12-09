# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 드래곤 커브의 개수
N = int(r_input())

grid = [[0] * 101 for _ in range(101)]      # 격자


def dragon_curve(stack, generate):
    generate -= 1

    tmp_stack = []

    for i in range(len(stack) - 1, -1, -1):
        tmp_stack.append([stack[-1][0] + (stack[-1][1] - stack[i][1]), stack[-1][1] - (stack[-1][0] - stack[i][0])])

    for loc in tmp_stack:
        grid[loc[0]][loc[1]] = 1

    stack.extend(tmp_stack)

    if generate:
        dragon_curve(stack, generate)


for _ in range(N):
    # x, y: 드래곤 커브 시작 지점, d: 시작 방향, g: 드래콘 커브 세대
    x, y, d, g = map(int, r_input().split())

    start_stack = [[x, y]]
    if d == 0:
        start_stack.append([x + 1, y])

    elif d == 1:
        start_stack.append([x, y - 1])

    elif d == 2:
        start_stack.append([x - 1, y])

    else:
        start_stack.append([x, y + 1])

    for l in start_stack:
        grid[l[0]][l[1]] = 1

    if g:
        dragon_curve(start_stack, g)

result = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i][j + 1] and grid[i + 1][j] and grid[i + 1][j + 1]:
            result += 1

print(result)

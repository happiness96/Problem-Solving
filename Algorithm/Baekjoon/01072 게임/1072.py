# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

x, y = map(int, r_input().split())          # x: 게임 횟수, y: 이긴 횟수
percentage = float(str(y / x)) * 100                    # 승률
percentage += 0.0000000001

aim = int(percentage) + 1
result = 0

if percentage >= 99:
    print(-1)
    exit()

while True:
    gap = aim / 100 * x - y
    
    if gap % 1:
        gap += 1

    gap = int(gap)

    x += gap
    y += gap

    result += gap

    if y / x * 100 >= aim:
        break

print(result)

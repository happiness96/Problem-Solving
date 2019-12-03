import sys
r_input = sys.stdin.readline

N = int(r_input())      # 기둥의 개수

roop = [0] * 1001
maximum = 0
over = 0

for _ in range(N):
    # L: 기둥의 왼쪽면위치, H: 기둥의 높이
    L, H = map(int, r_input().split())

    roop[L] = H

    if H > maximum:
        maximum = H

    if L > over:
        over = L

roop_left = roop.index(maximum)
roop_right = 1001 - roop[::-1].index(maximum)

height = 0
start = 0
area = 0

for i in range(roop_left + 1):      # 지붕의 왼쪽 면적
    if roop[i] > height:
        area += (i - start) * height
        height = roop[i]
        start = i

area += (roop_right - roop_left) * maximum      # 지붕의 중앙 면적

height = 0
start = 1001

for i in range(1000, roop_right-2, -1):         # 지붕의 오른쪽 면적
    if roop[i] > height:
        area += (start - i) * height
        height = roop[i]
        start = i

print(area)

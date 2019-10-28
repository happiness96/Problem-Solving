#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

coord = {}          # 팀원의 좌표

for i in range(3):
    x, y = map(int, r().split())
    
    if x in coord:
        coord[x].append(y)
    else:
        coord[x] = [y]


result = 0

if len(coord) == 1:         # 팀원들의 x축이 모두 같은 경우
    result = 1

if len(coord) ==2:          # 팀원들 중 두 명의 x축이 같은 경우
    result = 2

if len(coord) == 3:         # 팀원들의 x축이 모두 다른 경우
    x_s = sorted(coord)
    if (coord[x_s[0]][0] - coord[x_s[1]][0]) / (x_s[0] - x_s[1]) == (coord[x_s[1]][0] - coord[x_s[2]][0]) / (x_s[1] - x_s[2]):
        result = 1
    else:
        result = 2

print('WHERE IS MY CHICKEN?' if result == 1 else 'WINNER WINNER CHICKEN DINNER!' if result == 2 else '')

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

map_set = []

for i in range(16):
    map_set.append(list(map(int, r_input().split())))

while True:
    r, g, b = map(int, r_input().split())

    result_map = []
    D = 6367

    if r == g == b == -1:
        break

    for i in range(16):
        temp_D = ((map_set[i][0] - r)**2 + (map_set[i][1] - g)**2 + (map_set[i][2] - b)**2) ** 0.5
        if temp_D < D:
            D = temp_D
            result_map = map_set[i]

    print('(' + str(r) + ',' + str(g) + ',' + str(b) + ') maps to (' + str(result_map[0]) + ',' + str(result_map[1]) + ',' + str(result_map[2]) + ')')

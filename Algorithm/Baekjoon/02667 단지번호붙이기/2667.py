# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())      # N 지도의 크기 (N x N)
result = []

s_map = {0: ['0']*(N+2), N+1: ['0']*(N+2)}

for i in range(1, N+1):
    s_map[i] = ['0'] + list(r_input().rstrip()) + ['0']


def find_apartment(searching, cnt):            # 연결된 단지 찾기 (DFS)
    next_search = []

    while searching:
        loc = searching.pop()
        s_map[loc[0]][loc[1]] = '0'
        cnt += 1

        temp = [[loc[0]-1, loc[1]], [loc[0]+1, loc[1]], [loc[0], loc[1]-1], [loc[0], loc[1]+1]]

        for loc2 in temp:
            if s_map[loc2[0]][loc2[1]] == '1':
                if loc2 not in next_search:
                    next_search.append(loc2)

    if next_search:
        find_apartment(next_search, cnt)

    else:
        result.append(cnt)


for i in range(1, N+1):
    for j in range(1, N+1):
        if s_map[i][j] == '1':
            find_apartment([[i, j]], 0)

print(len(result))
for c in sorted(result):
    print(c)

# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

N = int(r_input())      # N 지도의 크기 (N x N)
searching = deque()
add1 = [0, 0, 1, -1]
add2 = [1, -1, 0, 0]
result = []

s_map = {0: ['0']*(N+2), N+1: ['0']*(N+2)}

for i in range(1, N+1):
    s_map[i] = ['0'] + list(r_input().rstrip()) + ['0']


def find_apartment(cnt):            # 연결된 단지 찾기 (DFS)
    while searching:
        loc = searching.popleft()
        s_map[loc[0]][loc[1]] = '0'
        cnt += 1

        for i in range(4):
            if s_map[loc[0] + add1[i]][loc[1] + add2[i]] == '1':
                if not [loc[0] + add1[i], loc[1] + add2[i]] in searching:
                    searching.append([loc[0] + add1[i], loc[1] + add2[i]])
    return cnt


for i in range(1, N+1):
    for j in range(1, N+1):
        if s_map[i][j] == '1':
            searching.append([i, j])
            result.append(find_apartment(0))

print(len(result))
for c in sorted(result):
    print(c)

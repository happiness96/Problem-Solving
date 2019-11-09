# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M= map(int, r_input().split())           # N x M

two_dots = {}

for i in range(N):
    s = r_input().rstrip()
    two_dots[i] = []
    for j in range(M):
        two_dots[i].append(s[j])


def find_connect(alpha, current, visit, final, start, move):            # final: 찾고자하는 좌표 (DFS)
    temp = [[current[0]-1, current[1]], [current[0]+1, current[1]], [current[0], current[1]-1], [current[0], current[1]+1]]

    if start == 0:
        visit.append(current)
        if current == final:
            print('Yes')
            exit()

    for loc in temp:
        if 0 <= loc[0] < N and 0 <= loc[1] < M:
            if two_dots[loc[0]][loc[1]] == alpha:
                if [loc[0], loc[1]] not in visit:

                    if move < 2 and loc == final:       # move가 2회 이상이여야 함
                        continue
                    
                    find_connect(alpha, [loc[0], loc[1]], visit, final, 0, move + 1)

    if start == 0:
        visit.append(current)


for i in range(N):
    for j in range(M):
        alpha = two_dots[i][j]
        find_connect(alpha, [i, j], [], [i, j], 1, 0)

print('No')

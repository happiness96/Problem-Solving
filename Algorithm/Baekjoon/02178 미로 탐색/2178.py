# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, M = map(int, r().split())            # N x M

maze = {}                               # 미로

for i in range(N):
    s = r().rstrip()
    maze[i] = []

    for j in range(len(s)):
        maze[i].append(int(s[j]))


def find_path(search_list, cnt):            # 다음 탐색 경로 찾기 (BFS)
    if [N-1, M-1] in search_list:       # 미로의 끝에 도달하면
        print(cnt)
        exit()
    
    next_search = []                    # 다음 탐색할 구간

    for path in search_list:
        temp = [[path[0]-1, path[1]], [path[0]+1, path[1]], [path[0], path[1]-1], [path[0], path[1]+1]]         # 사방을 체크

        maze[path[0]][path[1]] = 0          # 방문한 곳은 0으로 만들기

        for loc in temp:
            if 0 <= loc[0] < N and 0 <= loc[1] < M:
                if maze[loc[0]][loc[1]] == 1:       # 갈 수 있는 공간이라면
                    if not loc in next_search:
                        next_search.append(loc)

    find_path(next_search, cnt + 1)


find_path([[0, 0]], 1)

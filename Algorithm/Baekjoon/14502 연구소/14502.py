import sys
from itertools import combinations
r_input = sys.stdin.readline

# N: 지도의 세로 크기, M: 지도의 가로 크기
N, M = map(int, r_input().split())
result = 0          # 안전 영역의 최대 크기

board = {i: list(map(int, r_input().split())) for i in range(N)}

empty = []      # 빈 공간
wall = []       # 벽
virus = []      # 바이러스

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append([i, j])
        elif board[i][j] == 1:
            wall.append([i, j])
        else:
            virus.append([i, j])


def reset():            # 연구소 초기화
    for i, j in empty:
        board[i][j] = 0


def raise_wall(location):       # 벽 3개 세우기
    for l in location:
        board[l[0]][l[1]] = 1


def infect_virus():         # 바이러스 퍼짐 (BFS)
    global result
    visit = [[0] * M for _ in range(N)]

    stack = []

    for v in virus:
        visit[v[0]][v[1]] = 1
        stack.append(v)

    while stack:
        v = stack.pop()

        for i in range(4):
            tmp_x = v[0] + dx[i]
            tmp_y = v[1] + dy[i]

            if 0 <= tmp_x < N and 0 <= tmp_y < M:
                if not visit[tmp_x][tmp_y]:
                    if board[tmp_x][tmp_y] == 0:
                        visit[tmp_x][tmp_y] = 1
                        board[tmp_x][tmp_y] = 2
                        stack.append([tmp_x, tmp_y])

    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1

    if cnt > result:
        result = cnt


for loc in combinations(empty, 3):
    raise_wall(loc)
    infect_virus()
    reset()

print(result)

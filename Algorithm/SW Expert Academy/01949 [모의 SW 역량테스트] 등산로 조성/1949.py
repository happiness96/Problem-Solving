# -*- encoding: utf-8 -*-

# T: 테스트 케이스의 개수
T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find_root(loc, dig, dist):          # 등산로 찾기
    global result

    for k in range(4):
        tmp_row = loc[0] + dx[k]
        tmp_col = loc[1] + dy[k]

        flag = 1

        if 0 <= tmp_row < N and 0 <= tmp_col < N:
            if not visit[tmp_row][tmp_col]:
                if jido[tmp_row][tmp_col] < jido[loc[0]][loc[1]]:
                    visit[tmp_row][tmp_col] = 1
                    find_root([tmp_row, tmp_col], dig, dist + 1)
                    visit[tmp_row][tmp_col] = 0
                    flag = 0

                else:
                    if not dig:         # 현재 위치의 높이를 깎을 수 있다.
                        for deep in range(K):
                            jido[tmp_row][tmp_col] -= 1
                            if jido[tmp_row][tmp_col] < 0:
                                continue
                            if jido[tmp_row][tmp_col] < jido[loc[0]][loc[1]]:
                                visit[tmp_row][tmp_col] = 1
                                find_root([tmp_row, tmp_col], 1, dist + 1)
                                visit[tmp_row][tmp_col] = 0
                        jido[tmp_row][tmp_col] += K

                        flag = 0

        if flag:
            result = max(result, dist)


for t in range(T):
    # N: 지도 한 변의 길이, K: 최대 공사 가능 깊이
    N, K = map(int, input().split())

    jido = []
    max_height = 0      # 최대 높이

    for _ in range(N):
        info = list(map(int, input().split()))
        max_height = max(max_height, max(info))
        jido.append(info)

    locations = []          # 최대 높이 좌표

    for i in range(N):
        for j in range(N):
            if jido[i][j] == max_height:
                locations.append([i, j])

    result = 0

    visit=[[0] * N for _ in range(N)]

    for location in locations:
        visit[location[0]][location[1]] = 1
        find_root(location, 0, 1)
        visit[location[0]][location[1]] = 0

    print('#' + str(t + 1), result)

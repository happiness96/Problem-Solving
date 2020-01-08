# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    # 보물 지도의 가로, 세로 크기
    R, C = map(int, r_input().split())
    treasure_map = [list(r_input().rstrip()) for _ in range(R)]     # 보물 지도

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    result = 0

    for i in range(R):
        for j in range(C):
            if treasure_map[i][j] == 'L':
                visit = [[0] * C for _ in range(R)]

                visit[i][j] = 1
                dist = 0

                stack = [[i, j]]

                while True:
                    tmp_stack = []

                    while stack:
                        loc = stack.pop()

                        for k in range(4):
                            tmp_row = loc[0] + dr[k]
                            tmp_col = loc[1] + dc[k]

                            if 0 <= tmp_row < R and 0 <= tmp_col < C:
                                if not visit[tmp_row][tmp_col]:
                                    if treasure_map[tmp_row][tmp_col] == 'L':
                                        tmp_stack.append([tmp_row, tmp_col])
                                        visit[tmp_row][tmp_col] = 1

                    stack = tmp_stack

                    if not stack:
                        break

                    dist += 1

                if dist > result:
                    result = dist

    print(result)


run()

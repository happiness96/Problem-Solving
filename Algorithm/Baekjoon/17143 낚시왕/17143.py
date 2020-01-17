# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    # R, C: 격자의 크기
    # M: 상어의 수
    R, C, M = map(int, r_input().split())
    c_R = R - 1
    c_C = C - 1

    sharks = {}

    for _ in range(M):
        # r, c: 상어의 위치
        # s: 상어의 속도
        # d: 이동 방향 (1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽)
        # z: 크기
        r, c, s, d, z = map(int, r_input().split())

        if c not in sharks:
            sharks[c] = {}

        sharks[c][r] = [s, d, z]

    total = 0  # 낚시왕이 잡은 상어의 크기 합

    for loc in range(1, C + 1):
        # 상어 낚시
        if loc in sharks:
            shark = sharks[loc].pop(min(sharks[loc]))
            total += shark[2]

        # 상어 무빙
        tmp_sharks = {}

        for col in sharks:
            for row in sharks[col]:
                tmp = sharks[col][row]
                changed_row = 0
                changed_col = 0
                dist = tmp[0]
                way = 0

                if tmp[1] == 1:         # 위로 이동
                    changed_col = col

                    if row <= tmp[0]:
                        tmp[0] -= row - 1
                        turn = tmp[0] // c_R
                        mod = tmp[0] % c_R

                        if turn % 2:
                            way = 1
                            changed_row = R - mod

                        else:
                            way = 2
                            changed_row = 1 + mod

                    else:
                        way = 1
                        changed_row = row - tmp[0]
                    
                elif tmp[1] == 2:       # 아래로 이동
                    changed_col = col

                    gap = R - row

                    if gap < tmp[0]:
                        tmp[0] -= gap
                        turn = tmp[0] // c_R
                        mod = tmp[0] % c_R

                        if turn % 2:
                            way = 2
                            changed_row = 1 + mod

                        else:
                            way = 1
                            changed_row = R - mod

                    else:
                        way = 2
                        changed_row = row + tmp[0]
                
                elif tmp[1] == 3:       # 오른쪽으로 이동
                    changed_row = row

                    gap = C - col

                    if gap < tmp[0]:
                        tmp[0] -= gap
                        turn = tmp[0] // c_C
                        mod = tmp[0] % c_C

                        if turn % 2:
                            way = 3
                            changed_col = 1 + mod

                        else:
                            way = 4
                            changed_col = C - mod

                    else:
                        way = 3
                        changed_col = col + tmp[0]
                
                else:                   # 왼쪽으로 이동
                    changed_row = row

                    if col <= tmp[0]:
                        tmp[0] -= col - 1

                        turn = tmp[0] // c_C
                        mod = tmp[0] % c_C

                        if turn % 2:
                            way = 4
                            changed_col = C - mod

                        else:
                            way = 3
                            changed_col = 1 + mod

                    else:
                        way = 4
                        changed_col = col - tmp[0]

                if changed_col not in tmp_sharks:
                    tmp_sharks[changed_col] = {}

                if changed_row not in tmp_sharks[changed_col]:
                    tmp_sharks[changed_col][changed_row] = [dist, way, tmp[2]]

                elif tmp_sharks[changed_col][changed_row][2] < tmp[2]:
                    tmp_sharks[changed_col][changed_row] = [dist, way, tmp[2]]

        sharks = tmp_sharks

    print(total)


if __name__ == '__main__':
    run()

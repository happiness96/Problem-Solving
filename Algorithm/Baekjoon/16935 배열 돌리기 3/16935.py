# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


# 상하 반전
def inversion_top_down():
    for i in range(N // 2):
        array[i], array[N - i - 1] = array[N - i - 1], array[i]


# 좌우 반전
def inversion_left_right():
    for i in range(N):
        for j in range(M // 2):
            array[i][j], array[i][M - j - 1] = array[i][M - j - 1], array[i][j]


# 회전 (시계방향: 1, 반시계방향: 0)
def turn(clockwise: int) -> list:
    global N, M

    result_list: list = [[0] * N for _ in range(M)]

    for i in range(min(N, M) // 2):
        start = (0 + i, 0 + i)
        end = (N - i - 1, M - i - 1)

        save_list = []

        for i in range(start[1], end[1] + 1):
            save_list.append(array[start[0]][i])

        for i in range(start[0] + 1, end[0] + 1):
            save_list.append(array[i][end[1]])

        for i in range(end[1] - 1, start[0] - 1, -1):
            save_list.append(array[end[0]][i])

        for i in range(end[0] - 1, start[0], -1):
            save_list.append(array[i][start[0]])

        if clockwise:
            save_list = save_list[start[0] - end[0]:] + save_list[:start[0] - end[0]]

        else:
            save_list = save_list[end[1] - start[1]:] + save_list[:end[1] - start[1]]

        ind = 0
        for i in range(start[0], end[0] + 1):
            result_list[start[1]][i] = save_list[ind]
            ind += 1

        for i in range(start[1] + 1, end[1] + 1):
            result_list[i][end[0]] = save_list[ind]
            ind += 1

        for i in range(end[0] - 1, start[1] - 1, -1):
            result_list[end[1]][i] = save_list[ind]
            ind += 1

        for i in range(end[1] - 1, start[1], -1):
            result_list[i][start[1]] = save_list[ind]
            ind += 1

    N, M = M, N

    return result_list


# 분할
def division(flag):
    tmp_N = N // 2
    tmp_M = M // 2

    if flag == 5:
        for i in range(tmp_N):
            tmp = array[i][:tmp_M]

            tmp, array[i][tmp_M:] = array[i][tmp_M:], tmp
            tmp, array[tmp_N + i][tmp_M:] = array[tmp_N + i][tmp_M:], tmp
            tmp, array[tmp_N + i][:tmp_M] = array[tmp_N + i][:tmp_M], tmp

            array[i][:tmp_M] = tmp

    else:
        for i in range(tmp_N):
            tmp = array[i][:tmp_M]

            tmp, array[tmp_N + i][:tmp_M] = array[tmp_N + i][:tmp_M], tmp
            tmp, array[tmp_N + i][tmp_M:] = array[tmp_N + i][tmp_M:], tmp
            tmp, array[i][tmp_M:] = array[i][tmp_M:], tmp

            array[i][:tmp_M] = tmp


if __name__ == '__main__':
    # N x M 행렬, R회 회전
    N, M, R = map(int, r_input().split())

    array = [list(map(int, r_input().split())) for _ in range(N)]

    A = list(map(int, r_input().split()))      # 수행해야하는 연산

    for order in A:
        if order == 1:
            inversion_top_down()

        elif order == 2:
            inversion_left_right()

        elif order == 3:
            array = turn(1)

        elif order == 4:
            array = turn(0)

        else:
            division(order)

    for a in array:
        print(*a)

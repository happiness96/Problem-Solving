# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def rotate(start, end):
    circum = (end[0] - start[0] + 1) * 2 + (end[1] - start[1] - 1) * 2
    rot_cnt = R % circum

    tmp_list = []

    for i in range(start[0], end[0] + 1):
        tmp_list.append(array[i][start[1]])

    for i in range(start[1] + 1, end[1] + 1):
        tmp_list.append(array[end[0]][i])

    for i in range(end[0] - 1, start[0] - 1, -1):
        tmp_list.append(array[i][end[1]])

    for i in range(end[1] - 1, start[1], -1):
        tmp_list.append(array[start[0]][i])

    tmp_list = tmp_list[-rot_cnt:] + tmp_list[:-rot_cnt]
    ind = 0

    for i in range(start[0], end[0] + 1):
        array[i][start[1]] = tmp_list[ind]
        ind += 1

    for i in range(start[1] + 1, end[1] + 1):
        array[end[0]][i] = tmp_list[ind]
        ind += 1

    for i in range(end[0] - 1, start[0] - 1, -1):
        array[i][end[1]] = tmp_list[ind]
        ind += 1

    for i in range(end[1] - 1, start[1], -1):
        array[start[0]][i] = tmp_list[ind]
        ind += 1


if __name__ == '__main__':
    # N x M 행렬, R회 회전
    N, M, R = map(int, r_input().split())

    array = [list(map(int, r_input().split())) for _ in range(N)]

    for i in range(min(N, M) // 2):
        rotate((0 + i, 0 + i), (N - i - 1, M - i - 1))

    for a in array:
        print(*a)

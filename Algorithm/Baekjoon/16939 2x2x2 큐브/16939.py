# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def chk_cube():
    for i in range(6):
        t = 4 * i + 1

        if cube_list[t: t + 4] != [cube_list[t]] * 4:
            return 0

    return 1


def rotate(front, side):
    for _ in range(2):
        tmp = cube_list[front[0]]

        for i in range(1, 4):
            cube_list[front[i]], tmp = tmp, cube_list[front[i]]

        cube_list[front[0]] = tmp

        tmp = cube_list[side[0]]

        for i in range(1, 8):
            cube_list[side[i]], tmp = tmp, cube_list[side[i]]

        cube_list[side[0]] = tmp


def find_result():
    # 앞면 돌리기 (시계 방향)
    rotate([5, 6, 8, 7], [3, 4, 17, 19, 10, 9, 16, 14])
    if chk_cube():
        return 1
    rotate([7, 8, 6, 5], [14, 16, 9, 10, 19, 17, 4, 3])

    # 앞면 돌리기 (반시계 방향)
    rotate([7, 8, 6, 5], [14, 16, 9, 10, 19, 17, 4, 3])
    if chk_cube():
        return 1
    rotate([5, 6, 8, 7], [3, 4, 17, 19, 10, 9, 16, 14])

    # 뒷면 돌리기 (시계 방향)
    rotate([21, 22, 24, 23], [2, 1, 13, 15, 11, 12, 20, 18])
    if chk_cube():
        return 1
    rotate([23, 24, 22, 21], [18, 20, 12, 11, 15, 13, 1, 2])

    # 뒷면 돌리기 (반시계 방향)
    rotate([23, 24, 22, 21], [18, 20, 12, 11, 15, 13, 1, 2])
    if chk_cube():
        return 1
    rotate([21, 22, 24, 23], [2, 1, 13, 15, 11, 12, 20, 18])

    # 윗면 돌리기 (시계 방향)
    rotate([1, 2, 4, 3], [22, 21, 18, 17, 6, 5, 14, 13])
    if chk_cube():
        return 1
    rotate([3, 4, 2, 1], [13, 14, 5, 6, 17, 18, 21, 22])

    # 윗면 돌리기 (반시계 방향)
    rotate([3, 4, 2, 1], [13, 14, 5, 6, 17, 18, 21, 22])
    if chk_cube():
        return 1
    rotate([1, 2, 4, 3], [22, 21, 18, 17, 6, 5, 14, 13])

    # 밑면 돌리기 (시계 방향)
    rotate([9, 10, 12, 11], [7, 8, 19, 20, 23, 24, 15, 16])
    if chk_cube():
        return 1
    rotate([11, 12, 10, 9], [16, 15, 24, 23, 20, 19, 8, 7])

    # 밑면 돌리기 (반시계 방향)
    rotate([11, 12, 10, 9], [16, 15, 24, 23, 20, 19, 8, 7])
    if chk_cube():
        return 1
    rotate([9, 10, 12, 11], [7, 8, 19, 20, 23, 24, 15, 16])

    # 왼쪽면 돌리기 (시계 방향)
    rotate([13, 14, 16, 15], [1, 3, 5, 7, 9, 11, 24, 22])
    if chk_cube():
        return 1
    rotate([15, 16, 14, 13], [22, 24, 11, 9, 7, 5, 3, 1])

    # 왼쪽면 돌리기 (반시계 방향)
    rotate([15, 16, 14, 13], [22, 24, 11, 9, 7, 5, 3, 1])
    if chk_cube():
        return 1
    rotate([13, 14, 16, 15], [1, 3, 5, 7, 9, 11, 24, 22])

    # 오른쪽 면 돌리기 (시계 방향)
    rotate([17, 18, 20, 19], [4, 2, 21, 23, 12, 10, 8, 6])
    if chk_cube():
        return 1
    rotate([19, 20, 18, 17], [6, 8, 10, 12, 23, 21, 2, 4])

    # 오른쪽 면 돌리기 (반시계 방향)
    rotate([19, 20, 18, 17], [6, 8, 10, 12, 23, 21, 2, 4])
    if chk_cube():
        return 1
    rotate([17, 18, 20, 19], [4, 2, 21, 23, 12, 10, 8, 6])

    return 0


if __name__ == '__main__':
    cube_list = [0] + list(map(int, r_input().split()))
    print(find_result())

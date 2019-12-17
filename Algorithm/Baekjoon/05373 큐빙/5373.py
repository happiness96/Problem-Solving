# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def turn(side, clk):
    if clk == '+':      # 시계 방향
        side[0][0], side[0][1], side[0][2], side[1][2], side[2][2], side[2][1], side[2][0], side[1][0] = side[2][0], side[1][0], side[0][0], side[0][1], side[0][2], side[1][2], side[2][2], side[2][1]

    else:               # 반시계 방향
        side[0][2], side[0][1], side[0][0], side[1][0], side[2][0], side[2][1], side[2][2], side[1][2] = side[2][2], side[1][2], side[0][2], side[0][1], side[0][0], side[1][0], side[2][0], side[2][1]


t = int(r_input())

for _ in range(t):
    cube_u = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
    cube_d = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
    cube_f = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
    cube_b = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
    cube_l = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
    cube_r = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]

    n = int(r_input())      # 큐브를 돌린 횟수

    for order in map(str, r_input().rstrip().split()):
        if order[0] == 'U':
            turn(cube_u, order[1])
            if order[1] == '+':
                cube_f[0], cube_l[0], cube_b[0], cube_r[0] = cube_r[0], cube_f[0], cube_l[0], cube_b[0]
            else:
                cube_f[0], cube_l[0], cube_b[0], cube_r[0] = cube_l[0], cube_b[0], cube_r[0], cube_f[0]

        elif order[0] == 'D':
            turn(cube_d, order[1])
            if order[1] == '+':
                cube_f[2], cube_r[2], cube_b[2], cube_l[2] = cube_l[2], cube_f[2], cube_r[2], cube_b[2]
            else:
                cube_f[2], cube_r[2], cube_b[2], cube_l[2] = cube_r[2], cube_b[2], cube_l[2], cube_f[2]

        elif order[0] == 'F':
            turn(cube_f, order[1])
            if order[1] == '+':
                cube_u[2][0], cube_u[2][1], cube_u[2][2], cube_r[0][0], cube_r[1][0], cube_r[2][0], cube_d[2][0], cube_d[2][1], cube_d[2][2], cube_l[2][2], cube_l[1][2], cube_l[0][2] = cube_l[2][2], cube_l[1][2], cube_l[0][2], cube_u[2][0], cube_u[2][1], cube_u[2][2], cube_r[0][0], cube_r[1][0], cube_r[2][0], cube_d[2][0], cube_d[2][1], cube_d[2][2]
            else:
                cube_u[2][0], cube_u[2][1], cube_u[2][2], cube_r[0][0], cube_r[1][0], cube_r[2][0], cube_d[2][0], cube_d[2][1], cube_d[2][2], cube_l[2][2], cube_l[1][2], cube_l[0][2] = cube_r[0][0], cube_r[1][0], cube_r[2][0], cube_d[2][0], cube_d[2][1], cube_d[2][2], cube_l[2][2], cube_l[1][2], cube_l[0][2], cube_u[2][0], cube_u[2][1], cube_u[2][2]

        elif order[0] == 'B':
            turn(cube_b, order[1])
            if order[1] == '+':
                cube_u[0][2], cube_u[0][1], cube_u[0][0], cube_l[0][0], cube_l[1][0], cube_l[2][0], cube_d[0][2], cube_d[0][1], cube_d[0][0], cube_r[2][2], cube_r[1][2], cube_r[0][2] = cube_r[2][2], cube_r[1][2], cube_r[0][2], cube_u[0][2], cube_u[0][1], cube_u[0][0], cube_l[0][0], cube_l[1][0], cube_l[2][0], cube_d[0][2], cube_d[0][1], cube_d[0][0]
            else:
                cube_u[0][2], cube_u[0][1], cube_u[0][0], cube_l[0][0], cube_l[1][0], cube_l[2][0], cube_d[0][2], cube_d[0][1], cube_d[0][0], cube_r[2][2], cube_r[1][2], cube_r[0][2] = cube_l[0][0], cube_l[1][0], cube_l[2][0], cube_d[0][2], cube_d[0][1], cube_d[0][0], cube_r[2][2], cube_r[1][2], cube_r[0][2], cube_u[0][2], cube_u[0][1], cube_u[0][0]

        elif order[0] == 'L':
            turn(cube_l, order[1])
            if order[1] == '+':
                cube_u[0][0], cube_u[1][0], cube_u[2][0], cube_f[0][0], cube_f[1][0], cube_f[2][0], cube_d[2][2], cube_d[1][2], cube_d[0][2], cube_b[2][2], cube_b[1][2], cube_b[0][2] = cube_b[2][2], cube_b[1][2], cube_b[0][2], cube_u[0][0], cube_u[1][0], cube_u[2][0], cube_f[0][0], cube_f[1][0], cube_f[2][0], cube_d[2][2], cube_d[1][2], cube_d[0][2]
            else:
                cube_u[0][0], cube_u[1][0], cube_u[2][0], cube_f[0][0], cube_f[1][0], cube_f[2][0], cube_d[2][2], cube_d[1][2], cube_d[0][2], cube_b[2][2], cube_b[1][2], cube_b[0][2] = cube_f[0][0], cube_f[1][0], cube_f[2][0], cube_d[2][2], cube_d[1][2], cube_d[0][2], cube_b[2][2], cube_b[1][2], cube_b[0][2], cube_u[0][0], cube_u[1][0], cube_u[2][0]
        else:
            turn(cube_r, order[1])
            if order[1] == '+':
                cube_u[2][2], cube_u[1][2], cube_u[0][2], cube_b[0][0], cube_b[1][0], cube_b[2][0], cube_d[0][0], cube_d[1][0], cube_d[2][0], cube_f[2][2], cube_f[1][2], cube_f[0][2] = cube_f[2][2], cube_f[1][2], cube_f[0][2], cube_u[2][2], cube_u[1][2], cube_u[0][2], cube_b[0][0], cube_b[1][0], cube_b[2][0], cube_d[0][0], cube_d[1][0], cube_d[2][0]
            else:
                cube_u[2][2], cube_u[1][2], cube_u[0][2], cube_b[0][0], cube_b[1][0], cube_b[2][0], cube_d[0][0], cube_d[1][0], cube_d[2][0], cube_f[2][2], cube_f[1][2], cube_f[0][2] = cube_b[0][0], cube_b[1][0], cube_b[2][0], cube_d[0][0], cube_d[1][0], cube_d[2][0], cube_f[2][2], cube_f[1][2], cube_f[0][2], cube_u[2][2], cube_u[1][2], cube_u[0][2]

    for u in cube_u:
        print(''.join(u))

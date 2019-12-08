# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

gear = [0] + [r_input().rstrip() for _ in range(4)]
K = int(r_input())      # 회전 횟수


def rolling_gear(number, way):
    if way == 1:
        gear[number] = gear[number][-1] + gear[number][:-1]
    else:
        gear[number] = gear[number][1:] + gear[number][0]


for _ in range(K):
    num, direction = list(map(int, r_input().split()))

    chk = [not gear[1][2] == gear[2][6], not gear[2][2] == gear[3][6], not gear[3][2] == gear[4][6]]

    rolling_gear(num, direction)

    if num == 1:
        if chk[0]:
            rolling_gear(2, -direction)

            if chk[1]:
                rolling_gear(3, direction)

                if chk[2]:
                    rolling_gear(4, -direction)

    elif num == 2:
        if chk[0]:
            rolling_gear(1, -direction)

        if chk[1]:
            rolling_gear(3, -direction)

            if chk[2]:
                rolling_gear(4, direction)

    elif num == 3:
        if chk[2]:
            rolling_gear(4, -direction)

        if chk[1]:
            rolling_gear(2, -direction)

            if chk[0]:
                rolling_gear(1, direction)

    else:
        if chk[2]:
            rolling_gear(3, -direction)

            if chk[1]:
                rolling_gear(2, direction)

                if chk[0]:
                    rolling_gear(1, -direction)

total = 0
tmp = [0, 1, 2, 4, 8]

for i in range(1, 5):
    total += int(gear[i][0]) * tmp[i]

print(total)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

if __name__ == '__main__':
    C, P = map(int, r_input().split())

    blocks = list(map(int, r_input().split()))

    two_blocks = []
    three_blocks = []
    four_blocks = []

    result = [0] * 8

    if C > 1:
        two_blocks = [blocks[0], blocks[1]]

    if C > 2:
        three_blocks = [blocks[0], blocks[1], blocks[2]]

    if C > 3:
        four_blocks = [blocks[0], blocks[1], blocks[2], blocks[3]]

    for i in range(C):
        result[1] += 1

        if i < C - 1:
            if two_blocks[0] == two_blocks[1]:
                result[2] += 1
                result[6] += 1
                result[7] += 1

            elif two_blocks[0] == two_blocks[1] + 1:
                result[3] += 1
                result[5] += 1

            elif two_blocks[0] + 1 == two_blocks[1]:
                result[4] += 1
                result[5] += 1

            elif two_blocks[0] == two_blocks[1] + 2:
                result[6] += 1

            elif two_blocks[0] + 2 == two_blocks[1]:
                result[7] += 1

            if i != C - 2:
                two_blocks.pop(0)
                two_blocks.append(blocks[i + 2])

        if i < C - 2:
            if [three_blocks[0]] * 3 == three_blocks:
                result[5] += 1
                result[6] += 1
                result[7] += 1

            elif three_blocks[0] - 1 == three_blocks[1] == three_blocks[2]:
                result[4] += 1

            elif three_blocks[2] - 1 == three_blocks[0] == three_blocks[1]:
                result[3] += 1

            elif three_blocks[0] == three_blocks[2] == three_blocks[1] + 1:
                result[5] += 1

            elif three_blocks[0] + 1 == three_blocks[1] == three_blocks[2]:
                result[6] += 1

            elif three_blocks[2] + 1 == three_blocks[0] == three_blocks[1]:
                result[7] += 1

            if i != C - 3:
                three_blocks.pop(0)
                three_blocks.append(blocks[i + 3])

        if i < C - 3:
            if [four_blocks[0]] * 4 == four_blocks:
                result[1] += 1

            if i != C - 4:
                four_blocks.pop(0)
                four_blocks.append(blocks[i + 4])

    print(result[P])

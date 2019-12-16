# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def chk1(rect):
    for i in range(6):
        if rect[i].count(1) == 4:
            if 0 < i < 5:
                if rect[i - 1].count(1) and rect[i + 1].count(1):
                    return 1
            break

    return 0


def chk2(rect):
    for i in range(6):
        if rect[i].count(1) == 3:
            j = rect[i].index(1)

            if 1 < i < 5:
                if rect[i - 1][j + 1] and rect[i - 2][j + 1] and rect[i + 1].count(1):
                    return 1

            if 0 < i < 4:
                if rect[i + 1][j + 1] and rect[i + 2][j + 1] and rect[i - 1].count(1):
                    return 1

            if 0 < i < 5 and 0 < j:
                if rect[i - 1][j] and rect[i - 1][j - 1] and rect[i + 1].count(1):
                    return 1

            if 0 < i < 5 and j <= 2:
                if rect[i - 1][j + 2] and rect[i - 1][j + 3] and rect[i + 1].count(1):
                    return 1

            if 0 < i < 5 and 0 < j:
                if rect[i + 1][j] and rect[i + 1][j - 1] and rect[i - 1].count(1):
                    return 1

            if 0 < i < 5 and j <= 2:
                if rect[i + 1][j + 2] and rect[i + 1][j + 3] and rect[i - 1].count(1):
                    return 1

            if i < 5 and j < 2:
                if rect[i + 1][j + 2] and rect[i + 1][j + 3] and rect[i + 1][j + 4]:
                    return 1

            if i < 5 and 2 <= j <= 3:
                if rect[i + 1][j] and rect[i + 1][j - 1] and rect[i + 1][j - 2]:
                    return 1

            break
    return 0


def chk3(rect):
    for i in range(6):
        if rect[i].count(1) == 2:
            j = rect[i].index(1)

            if i < 4 and j < 3:
                if rect[i + 1][j + 1] and rect[i + 1][j + 2] and rect[i + 2][j + 2] and rect[i + 2][j + 3]:
                    return 1

            if i < 4 and j > 1:
                if rect[i + 1][j] and rect[i + 1][j - 1] and rect[i + 2][j - 1] and rect[i + 2][j - 2]:
                    return 1

            break

    return 0


for _ in range(3):
    rect1 = [list(map(int, r_input().split())) for _ in range(6)]
    rect2 = [[rect1[a][b] for a in range(6)] for b in range(6)]

    if chk1(rect1):
        print('yes')
        continue

    if chk1(rect2):
        print('yes')
        continue

    if chk2(rect1):
        print('yes')
        continue

    if chk2(rect2):
        print('yes')
        continue

    if chk3(rect1):
        print('yes')
        continue

    if chk3(rect2):
        print('yes')
        continue

    print('no')

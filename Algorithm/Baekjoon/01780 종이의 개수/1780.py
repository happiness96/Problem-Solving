# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(r_input())          # 종이의 크기

paper = {}
minus = 0
zero = 0
plus = 0

for i in range(N):
    paper[i] = list(map(int, r_input().split()))


def find_paper(start_x, start_y, size):        # 분할 정복
    global minus
    global zero
    global plus

    comp = paper[start_x][start_y]

    div = 0

    for i in range(start_x, start_x + size):
        if paper[i][start_y:start_y + size] != [comp] * size:
            div = 1
            break

        if div:
            break

    if div:
        size //= 3

        for i in range(3):
            for j in range(3):
                find_paper(start_x + size * i, start_y + size * j, size)

    else:
        if comp == -1:
            minus += 1

        elif comp == 0:
            zero += 1

        else:
            plus += 1


find_paper(0, 0, N)

print(minus)
print(zero)
print(plus)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())

if N % 2:
    print(0)
    exit()

total = 0


def dfs(num, save):
    global total

    if sum(save) > N:
        return

    if sum(save) == N:
        total += 3 ** save.count(2) * 2 ** (len(save) - save.count(2))

    else:
        for i in range(2, N + 1, 2):
            dfs(i, save + [i])


for i in range(2, N + 1, 2):
    dfs(i, [i])

print(total)

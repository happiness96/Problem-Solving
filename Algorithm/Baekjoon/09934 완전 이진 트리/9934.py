# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

K = int(r_input())

building = list(map(str, r_input().rstrip().split()))[::-1]

tree = [[] for _ in range(K)]


def run(level):
    if level == K - 1:
        tree[level].append(building.pop())
        return

    run(level + 1)

    tree[level].append(building.pop())

    run(level + 1)


run(0)

for i in range(K):
    print(' '.join(tree[i]))

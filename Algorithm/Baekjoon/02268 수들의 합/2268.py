# -*- encoding: utf-8 -*-
import sys
from math import *
r_input = sys.stdin.readline


def modify(node, start, end):
    if not start <= b <= end:
        return

    seg_tree[node] += gap

    if start != end:
        mid = (start + end) // 2
        modify(node * 2, start, mid)
        modify(node * 2 + 1, mid + 1, end)


def get_sum(node, start, end, left, right):
    global total

    if end < left or start > right:
        return

    if left <= start and end <= right:
        total += seg_tree[node]

    else:
        mid = (start + end) // 2
        get_sum(node * 2, start, mid, left, right)
        get_sum(node * 2 + 1, mid + 1, end, left, right)


if __name__ == '__main__':
    N, M = map(int, r_input().split())

    array = [0] * (N + 1)
    size = 2 ** (ceil(log2(N)) + 1)
    seg_tree = [0] * size

    for _ in range(M):
        a, b, c = map(int, r_input().split())

        if a == 0:
            if b > c:
                b, c = c, b
            total = 0
            get_sum(1, 1, N, b, c)
            print(total)

        else:
            gap = c - array[b]
            modify(1, 1, N)
            array[b] = c

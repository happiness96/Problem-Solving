# -*- encoding: utf-8 -*-
import sys
from math import *
r_input = sys.stdin.readline


def seg_init(node, start, end):
    if start == end:
        seg_tree[node] = array[start]
        return array[start]

    mid = (start + end) // 2

    left = seg_init(node * 2, start, mid)
    right = seg_init(node * 2 + 1, mid + 1, end)

    seg_tree[node] = min(left, right)

    return seg_tree[node]


def get_result(node, start, end, left, right):
    global result

    if end < left or start > right:
        return

    if left <= start and end <= right:
        result = min(result, seg_tree[node])

    else:
        mid = (start + end) // 2
        get_result(node * 2, start, mid, left, right)
        get_result(node * 2 + 1, mid + 1, end, left, right)


if __name__ == '__main__':
    N, M = map(int, r_input().split())

    array = [0] + [int(r_input()) for _ in range(N)]

    size = 2 ** int(ceil(log2(N)) + 1)
    seg_tree = [0] * size

    seg_init(1, 1, N)

    for _ in range(M):
        a, b = map(int, r_input().split())

        result = sys.maxsize
        get_result(1, 1, N, a, b)
        print(result)

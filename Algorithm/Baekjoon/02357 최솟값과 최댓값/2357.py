# -*- encoding: utf-8 -*-
import sys
from math import *
r_input = sys.stdin.readline


def min_seg_init(node, start, end):
    if start == end:
        min_seg_tree[node] = array[start]
        return array[start]

    mid = (start + end) // 2

    left = min_seg_init(node * 2, start, mid)
    right = min_seg_init(node * 2 + 1, mid + 1, end)

    min_seg_tree[node] = min(left, right)

    return min_seg_tree[node]


def max_seg_init(node, start, end):
    if start == end:
        max_seg_tree[node] = array[start]
        return array[start]

    mid = (start + end) // 2

    left = max_seg_init(node * 2, start, mid)
    right = max_seg_init(node * 2 + 1, mid + 1, end)

    max_seg_tree[node] = max(left, right)

    return max_seg_tree[node]


def get_min_result(node, start, end, left, right):
    global min_result

    if end < left or start > right:
        return

    if left <= start and end <= right:
        min_result = min(min_result, min_seg_tree[node])

    else:
        mid = (start + end) // 2
        get_min_result(node * 2, start, mid, left, right)
        get_min_result(node * 2 + 1, mid + 1, end, left, right)


def get_max_result(node, start, end, left, right):
    global max_result

    if end < left or start > right:
        return

    if left <= start and end <= right:
        max_result = max(max_result, max_seg_tree[node])

    else:
        mid = (start + end) // 2
        get_max_result(node * 2, start, mid, left, right)
        get_max_result(node * 2 + 1, mid + 1, end, left, right)


if __name__ == '__main__':
    N, M = map(int, r_input().split())

    array = [0] + [int(r_input()) for _ in range(N)]

    size = 2 ** int(ceil(log2(N)) + 1)
    min_seg_tree = [0] * size
    max_seg_tree = [0] * size

    min_seg_init(1, 1, N)
    max_seg_init(1, 1, N)

    for _ in range(M):
        a, b = map(int, r_input().split())

        min_result = sys.maxsize
        max_result = 0

        get_min_result(1, 1, N, a, b)
        get_max_result(1, 1, N, a, b)

        print(min_result, max_result)

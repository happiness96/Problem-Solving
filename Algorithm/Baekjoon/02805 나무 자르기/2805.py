# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

def run():
    # N: 나무의 개수, M: 집으로 가져가려하는 나무의 높이
    N, M = map(int, r_input().split())
    tree = list(map(int, r_input().split()))

    result = 0

    l, r = 0, max(tree)

    while True:
        tmp = (r + l) // 2
        total = 0

        for t in tree:
            if t > tmp:
                total += t - tmp

        if total >= M:
            result = tmp
            l = tmp

        else:
            r = tmp

        if r - l == 1:
            break

        # print(tmp)

    print(result)


run()

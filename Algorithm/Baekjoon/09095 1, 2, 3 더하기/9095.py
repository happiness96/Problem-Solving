# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

T = int(r_input())      # T: 테스트 케이스의 개수


def find_cnt(sum_list):         # 경우의 수 찾기
    global cnt
    total = sum(sum_list)

    if total == n:
        cnt += 1

    elif total < n:
        find_cnt(sum_list + [1])
        find_cnt(sum_list + [2])
        find_cnt(sum_list + [3])


for _ in range(T):
    n = int(r_input())
    cnt = 0             # 1, 2, 3 의 합으로 나타낼 수 있는 경우의 수

    find_cnt([1])
    find_cnt([2])
    find_cnt([3])

    print(cnt)

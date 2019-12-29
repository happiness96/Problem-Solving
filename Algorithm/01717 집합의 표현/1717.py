# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# n: n + 1개의 집합, m: 연산의 개수
n, m = map(int, r_input().split())
save = list(range(n + 1))


def get_parent(num):
    if save[num] != num:
        save[num] = get_parent(save[num])

    return save[num]


def union(num1, num2):
    p1 = get_parent(num1)
    p2 = get_parent(num2)

    if p1 < p2:
        save[p2] = p1
    else:
        save[p1] = p2


def find(num1, num2):
    p1 = get_parent(num1)
    p2 = get_parent(num2)

    if p1 == p2:
        print('YES')
    else:
        print('NO')


for _ in range(m):
    order, a, b = map(int, r_input().split())

    if order == 0:
        union(a, b)

    else:
        find(a, b)

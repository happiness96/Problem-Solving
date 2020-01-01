# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# T: 테스트 케이스의 개수
T = int(r_input())


def get_parent(name):
    if parent[name] != name:
        parent[name] = get_parent(parent[name])

    return parent[name]


def union(friend1, friend2):
    parent1 = get_parent(friend1)
    parent2 = get_parent(friend2)

    if parent1 < parent2:
        parent[parent2] = parent1

    else:
        parent[parent1] = parent2


def find(friend1, friend2):
    parent1 = get_parent(friend1)
    parent2 = get_parent(friend2)

    print(1 if parent1 == parent2 else 0)


for t in range(1, T + 1):
    # n: 유저의 수
    n = int(r_input())

    parent = list(range(n))

    # k: 친구 관계의 수
    k = int(r_input())

    for _ in range(k):
        a, b = map(int, r_input().split())
        union(a, b)

    # 구할 쌍의 개수
    m = int(r_input())

    print('Scenario ' + str(t) + ':')

    for _ in range(m):
        a, b = map(int, r_input().split())
        find(a, b)

    print()

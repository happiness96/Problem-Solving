# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def get_parent(name):
    if parent[name] != name:
        parent[name] = get_parent(parent[name])

    return parent[name]


def union(name1, name2):
    p1 = get_parent(name1)
    p2 = get_parent(name2)

    if p1 < p2:
        for member in group[p2]:
            parent[member] = p1
        group[p1].extend(group[p2])
        print(len(group[p1]))

    elif p1 > p2:
        for member in group[p1]:
            parent[member] = p2
        group[p2].extend(group[p1])
        print(len(group[p2]))

    else:
        print(len(group[p1]))


# t: 테스트 케이스의 개수
t = int(r_input())

for _ in range(t):
    parent = {}
    group = {}

    # F: 친구 관계의 수
    F = int(r_input())

    for _ in range(F):
        # 친구 관계인 두 친구
        friend1, friend2 = map(str, r_input().rstrip().split())

        chk1 = friend1 in parent
        chk2 = friend2 in parent

        if not chk1 and not chk2:  # 둘 다 처음 등장하는 경우
            if friend1 < friend2:
                parent[friend1] = friend1
                parent[friend2] = friend1
                group[friend1] = [friend1, friend2]

            else:
                parent[friend2] = friend2
                parent[friend1] = friend2
                group[friend2] = [friend1, friend2]

            print(2)

        elif not chk2:  # friend1은 이미 한번 등장한 경우
            p = get_parent(friend1)
            parent[friend2] = p
            group[p].append(friend2)
            print(len(group[p]))

        elif not chk1:
            p = get_parent(friend2)
            parent[friend1] = p
            group[p].append(friend1)
            print(len(group[p]))

        else:
            union(friend1, friend2)

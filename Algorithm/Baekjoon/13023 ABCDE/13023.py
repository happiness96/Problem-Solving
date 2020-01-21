# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def find_friend(node, cnt):
    if cnt == 5:
        print(1)
        exit()

    for f in friends[node]:
        if not visit[f]:
            visit[f] = 1
            find_friend(f, cnt + 1)
            visit[f] = 0


if __name__ == '__main__':
    N, M = map(int, r_input().split())

    friends = {num: [] for num in range(N)}

    for _ in range(M):
        a, b = map(int, r_input().split())

        friends[a].append(b)
        friends[b].append(a)

    visit = [0] * N
    for i in range(N):
        visit[i] = 1
        find_friend(i, 1)
        visit[i] = 0

    print(0)

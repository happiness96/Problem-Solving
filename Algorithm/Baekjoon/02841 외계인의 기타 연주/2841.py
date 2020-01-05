# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 멜로디에 포함되어 있는 음의 수, P: 한 줄에 있는 프렛의 수
N, P = map(int, r_input().split())
line = [[] for _ in range(7)]
cnt = 0

for _ in range(N):
    a, b = map(int, r_input().split())

    while True:
        if not line[a]:
            cnt += 1
            line[a].append(b)
            break

        elif line[a][-1] > b:
            cnt += 1
            line[a].pop()

        elif line[a][-1] == b:
            break

        else:
            cnt += 1
            line[a].append(b)
            break

print(cnt)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 회의의 수
N = int(r_input())

save = {}

for _ in range(N):
    # 회의 시작 시간, 끝나는 시간
    start, end = map(int, r_input().split())

    if end in save:
        save[end].append(start)

    else:
        save[end] = [start]

cnt = 0
tmp = 0

for t in sorted(save):
    for a in sorted(save[t]):
        if a >= tmp:
            tmp = t
            cnt += 1

print(cnt)

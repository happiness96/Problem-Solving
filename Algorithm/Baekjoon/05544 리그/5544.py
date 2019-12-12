# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 팀의 수
N = int(r_input())

score = {num: 0 for num in range(1, N + 1)}

for _ in range(N * (N - 1) // 2):
    A, B, C, D = map(int, r_input().split())

    if C > D:
        score[A] += 3

    elif D > C:
        score[B] += 3

    else:
        score[A] += 1
        score[B] += 1


rank = {v: [] for v in score.values()}

for s in score:
    rank[score[s]].append(s)


result = [0] * (N + 1)
tmp = 1

for r in sorted(rank)[::-1]:
    for c in rank[r]:
        result[c] = str(tmp)
    tmp += len(rank[r])


print('\n'.join(result[1:]))

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 플레이어의 수, M: 가진 카드 수
N, M = map(int, r_input().split())
save = [sorted(map(int, r_input().split())) for _ in range(N)]

score = [0] * N

for _ in range(M):
    turn = [save[i].pop() for i in range(N)]
    maximum = max(turn)

    for i in range(N):
        if turn[i] == maximum:
            score[i] += 1

max_score = max(score)

for i in range(N):
    if score[i] == max_score:
        print(i + 1, end=' ')

# -*- encoding: utf-8 -*-
import sys
from itertools import combinations
r_input = sys.stdin.readline

N = int(r_input())      # N: 사람의 수
num = [i for i in range(1, N+1)]
S = {}          # 사람의 능력치
result = 14889

for i in range(1, N+1):
    S[i] = [0] + list(map(int, r_input().split()))


def find_gap(team_s):       # 두 팀의 능력치 차이
    global result
    start_score = 0                 # 스타트팀의 능력치
    link_score = 0                  # 링크 팀의 능력치

    for i in range(1, N+1):
        if i in team_s:
            for j in team_s:
                start_score += S[i][j]

        else:
            for j in range(1, N+1):
                if j not in team_s:
                    link_score += S[i][j]

    result = min(abs(start_score - link_score), result)

    if result == 0:
        print(result)
        exit()


for start in combinations(num, N//2):
    if start[0] != 1:
        break

    find_gap(start)

print(result)

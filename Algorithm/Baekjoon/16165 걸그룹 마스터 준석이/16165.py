# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())      # N: 걸그룹의 수, M: 문제의 수
girl_group = {}             # 걸그룹

for _ in range(N):
    team = r_input().rstrip()     # 걸그룹 팀 이름
    girl_group[team] = []

    n = int(r_input())      # 인원 수

    for _ in range(n):
        girl_group[team].append(r_input().rstrip())

for _ in range(M):              # 퀴즈
    name = r_input().rstrip()       # 팀 이름이나 멤버의 이름
    quiz = int(r_input())           # 퀴즈의 유형

    if quiz:            # 멤버의 이름이 주어진 경우
        for team_name in girl_group:
            if name in girl_group[team_name]:
                print(team_name)

    else:               # 팀의 이름이 주어진 경우
        for member in sorted(girl_group[name]):
            print(member)

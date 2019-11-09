# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# n: 참가한 팀의 수, m: 문제의 수, q: 채점 로그의 개수
n, m, q = map(int, r_input().split())

solved = {}             # 문제를 푼 팀
problem_cnt = [0] * (n+1)           # 각 팀별 푼 문제 수
total_time = [0] * (n+1)            # 각 팀별 경과 시간
team_log = {}                       # 각 팀별 문제 로그

for i in range(1, m+1):
    solved[i] = []

for i in range(1, n+1):
    team_log[i] = [0] * (m+1)

for _ in range(q):
    # time: 경과 시간, team_num: 팀 번호, pro_num: 문제 번호, result: 결과
    time, team_num, pro_num, result = map(str, r_input().rstrip().split())

    time = int(time)
    team_num = int(team_num)
    pro_num = int(pro_num)

    if result != 'AC':              # 문제를 맞추지 못했다면
        team_log[team_num][pro_num] += 1

    else:                           # 문제를 맞췄다면
        if team_num not in solved[pro_num]:         # 이전에 푼 이력이 없다면
            solved[pro_num].append(team_num)
            problem_cnt[team_num] += 1
            total_time[team_num] += time + 20 * team_log[team_num][pro_num]

get_result = {}
for i in range(1, n+1):
    if problem_cnt[i] not in get_result:
        get_result[problem_cnt[i]] = {}
        get_result[problem_cnt[i]][total_time[i]] = [i]

    else:
        if total_time[i] in get_result[problem_cnt[i]]:
            get_result[problem_cnt[i]][total_time[i]].append(i)

        else:
            get_result[problem_cnt[i]][total_time[i]] = [i]

for c in sorted(get_result)[::-1]:
    for d in sorted(get_result[c]):
        for e in sorted(get_result[c][d]):
            print(e, c, d)

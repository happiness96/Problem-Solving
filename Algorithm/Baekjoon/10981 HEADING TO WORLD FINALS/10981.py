# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

N, K = map(int, r().split())            # N: 팀의 수, K: 진출할 대학의 수

each_rank = {}
rank = {}

for i in range(N):
    school, team, solve, penalty = map(str, r().rstrip().split())
    solve = int(solve)
    penalty = int(penalty)

    if not school in each_rank:
        each_rank[school] = [solve, penalty, team]
    else:
        if solve > each_rank[school][0]:
            each_rank[school] = [solve, penalty, team]
        elif solve == each_rank[school][0]:
            if penalty < each_rank[school][1]:
                each_rank[school] = [solve, penalty, team]

for school_name in each_rank:
    if not each_rank[school_name][0] in rank:
        rank[each_rank[school_name][0]] = {each_rank[school_name][1]:each_rank[school_name][2]}
    else:
        rank[each_rank[school_name][0]][each_rank[school_name][1]] = each_rank[school_name][2]

cnt = 0
for i in sorted(rank, reverse = True):
    for j in sorted(rank[i]):
        print(rank[i][j])
        cnt += 1
        if cnt == K:
            exit()

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    T = int(r_input())

    for _ in range(T):
        n, k, t, m = map(int, r_input().split())

        solved = {team_no: {problem_no: 0 for problem_no in range(1, k + 1)} for team_no in range(1, n + 1)}
        submit_cnt = [0] * (n + 1)
        last_submit = [0] * (n + 1)

        for log_no in range(m):
            i, j, s = map(int, r_input().split())

            if solved[i][j] < s:
                solved[i][j] = s

            last_submit[i] = log_no
            submit_cnt[i] += 1

        score = {}

        for team_no in solved:
            sc = 0
            for problem_no in solved[team_no]:
                sc += solved[team_no][problem_no]
            submit = submit_cnt[team_no]
            last = last_submit[team_no]

            if sc not in score:
                score[sc] = {}

            if submit not in score[sc]:
                score[sc][submit] = {}

            score[sc][submit][last] = team_no

        ranking = 1
        flag = 0

        for s in sorted(score, reverse=True):
            for m in sorted(score[s]):
                for l in sorted(score[s][m]):
                    if score[s][m][l] == t:
                        print(ranking)
                        flag = 1
                        break

                    ranking += 1
                if flag:
                    break

            if flag:
                break


if __name__ == '__main__':
    run()

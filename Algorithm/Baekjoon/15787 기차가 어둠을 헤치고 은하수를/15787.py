# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

if __name__ == '__main__':
    # N: 기차의 수, M: 명령의 수
    N, M = map(int, r_input().split())

    trains = {train_no: [0] * 20 for train_no in range(1, N + 1)}

    for _ in range(M):
        order = list(map(int, r_input().split()))

        if order[0] == 1:
            trains[order[1]][order[2] - 1] = 1

        elif order[0] == 2:
            trains[order[1]][order[2] - 1] = 0

        elif order[0] == 3:
            trains[order[1]] = [0] + trains[order[1]][:-1]

        else:
            trains[order[1]] = trains[order[1]][1:] + [0]

    visit = []
    result = 0

    for t_v in trains.values():
        if t_v not in visit:
            visit.append(t_v)
            result += 1

    print(result)

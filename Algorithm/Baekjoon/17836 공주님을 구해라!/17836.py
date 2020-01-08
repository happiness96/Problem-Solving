# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    # N, M: 성의 크기
    # T: 공주에게 걸린 저주의 제한 시간
    N, M, T = map(int, r_input().split())

    castle = [list(map(int, r_input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]

    queue = [[[0, 0]], []]
    hour = 0
    visit[0][0] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    dest = [N - 1, M - 1]

    while hour <= T:
        tmp_queue = [[], []]

        for _ in range(len(queue[0])):
            loc = queue[0].pop()

            if loc == dest:
                print(hour)
                exit()

            for k in range(4):
                tmp_row = loc[0] + dx[k]
                tmp_col = loc[1] + dy[k]

                if 0 <= tmp_row < N and 0 <= tmp_col < M:
                    if not visit[tmp_row][tmp_col]:
                        if not castle[tmp_row][tmp_col]:
                            tmp_queue[0].append([tmp_row, tmp_col])
                            visit[tmp_row][tmp_col] = 1

                        if castle[tmp_row][tmp_col] == 2:
                            tmp_queue[1].append([tmp_row, tmp_col])
                            visit[tmp_row][tmp_col] = 2

        for _ in range(len(queue[1])):
            loc = queue[1].pop()

            if loc == dest:
                print(hour)
                exit()

            for k in range(4):
                tmp_row = loc[0] + dx[k]
                tmp_col = loc[1] + dy[k]

                if 0 <= tmp_row < N and 0 <= tmp_col < M:
                    if not visit[tmp_row][tmp_col] == 2:
                        tmp_queue[1].append([tmp_row, tmp_col])
                        visit[tmp_row][tmp_col] = 2

        queue = tmp_queue

        hour += 1

    print('Fail')


if __name__ == '__main__':
    run()

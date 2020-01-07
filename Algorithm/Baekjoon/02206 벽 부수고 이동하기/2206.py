# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    # 맵의 크기
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    N, M = map(int, r_input().split())

    board = [[int(num) for num in r_input().rstrip()] for _ in range(N)]
    visit = [[0] * M for _ in range(N)]

    # [row, col, broken]
    zero_queue = [[0, 0]]
    one_queue = []
    visit[0][0] = 1

    dist = 1
    result = [N - 1, M - 1]

    while zero_queue or one_queue:
        tmp_zero_queue = []
        tmp_one_queue = []

        while zero_queue:
            loc = zero_queue.pop()

            if loc == result:
                print(dist)
                exit()

            for k in range(4):
                tmp_row = loc[0] + dx[k]
                tmp_col = loc[1] + dy[k]

                if 0 <= tmp_row < N and 0 <= tmp_col < M:
                    if visit[tmp_row][tmp_col] != 1:
                        if not board[tmp_row][tmp_col]:
                            tmp_zero_queue.append([tmp_row, tmp_col])
                            visit[tmp_row][tmp_col] = 1

                        elif visit[tmp_row][tmp_col] != 2:
                            tmp_one_queue.append([tmp_row, tmp_col])
                            visit[tmp_row][tmp_col] = 2

        while one_queue:
            loc = one_queue.pop()

            if loc == result:
                print(dist)
                exit()

            for k in range(4):
                tmp_row = loc[0] + dx[k]
                tmp_col = loc[1] + dy[k]

                if 0 <= tmp_row < N and 0 <= tmp_col < M:
                    if not visit[tmp_row][tmp_col]:
                        if not board[tmp_row][tmp_col]:
                            tmp_one_queue.append([tmp_row, tmp_col])
                            visit[tmp_row][tmp_col] = 2

        dist += 1
        zero_queue = tmp_zero_queue
        one_queue = tmp_one_queue

    print(-1)


if __name__ == '__main__':
    run()

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    N, M, B = map(int, r_input().split())

    result_time = sys.maxsize
    result_height = 0

    minimum = 256

    board = []
    for _ in range(N):
        line = list(map(int, r_input().split()))

        minimum = min(minimum, min(line))

        board.append(line)

    for height in range(minimum, 257):
        time = 0

        blocks = B

        for i in range(N):
            for j in range(M):
                if board[i][j] > height:
                    time += 2 * (board[i][j] - height)
                    blocks += board[i][j] - height
                else:
                    time += height - board[i][j]
                    blocks -= height - board[i][j]

        if blocks >= 0:
            if time < result_time:
                result_time = time
                result_height = height

            elif time == result_time:
                result_height = height
        else:
            break

    print(result_time, result_height)


if __name__ == '__main__':
    run()

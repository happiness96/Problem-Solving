# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline


def run():
    r, c, k = map(int, r_input().split())

    r -= 1
    c -= 1

    A = [list(map(int, r_input().split())) for _ in range(3)]

    cnt_row = 3
    cnt_col = 3

    time = 0

    while True:
        if cnt_row >= r + 1 and cnt_col >= c + 1 and A[r][c] == k:
            break

        if time > 100:
            print(-1)
            sys.exit()

        if cnt_row >= cnt_col:
            # R 연산
            max_size = 0
            save_queue = [[] for _ in range(cnt_row)]

            for row in range(cnt_row):
                number_count = {}
                for number in A[row]:
                    if number == 0:
                        continue
                    if number not in number_count:
                        number_count[number] = 0
                    number_count[number] += 1

                max_size = min(100, max(max_size, 2 * len(number_count)))

                for number in number_count:
                    save_queue[row].append((number_count[number], number))

            A = [[0] * max_size for _ in range(cnt_row)]
            cnt_col = max_size

            for row in range(cnt_row):
                heapify(save_queue[row])
                ind = 0

                while save_queue[row]:
                    case = heappop(save_queue[row])
                    A[row][ind] = case[1]
                    A[row][ind + 1] = case[0]
                    ind += 2

                if ind == 100:
                    break

        else:
            # C 연산
            max_size = 0
            save_queue = [[] for _ in range(cnt_col)]

            for col in range(cnt_col):
                number_count = {}

                for row in range(cnt_row):
                    number = A[row][col]
                    if number == 0:
                        continue

                    if number not in number_count:
                        number_count[number] = 0

                    number_count[number] += 1

                max_size = min(100, max(max_size, 2 * len(number_count)))

                for number in number_count:
                    save_queue[col].append((number_count[number], number))

            A = [[0] * cnt_col for _ in range(max_size)]
            cnt_row = max_size

            for col in range(cnt_col):
                heapify(save_queue[col])
                ind = 0

                while save_queue[col]:
                    case = heappop(save_queue[col])
                    A[ind][col] = case[1]
                    A[ind + 1][col] = case[0]
                    ind += 2

                if ind == 100:
                    break

        time += 1

    print(time)


if __name__ == '__main__':
    run()

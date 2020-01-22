# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    N, k = map(int, r_input().split())

    line1 = list(r_input().rstrip())
    line2 = list(r_input().rstrip())

    visit1 = [0] * N
    visit2 = [0] * N

    queue1 = [0]
    queue2 = []

    visit1[0] = 1

    for i in range(N):
        tmp_queue1 = []
        tmp_queue2 = []

        if not queue1 and not queue2:
            break

        line1[i] = '0'
        line2[i] = '0'

        while queue1:
            loc = queue1.pop()
            tmp_loc = [loc - 1, loc + 1]

            for moved_loc in tmp_loc:
                if moved_loc >= N:
                    print(1)
                    exit()

                if 0 <= moved_loc < N:
                    if not visit1[moved_loc] and line1[moved_loc] == '1':
                        tmp_queue1.append(moved_loc)
                        visit1[moved_loc] = 1

            moved_loc = loc + k
            if moved_loc >= N:
                print(1)
                exit()

            if 0 <= moved_loc < N:
                if not visit2[moved_loc] and line2[moved_loc] == '1':
                    tmp_queue2.append(moved_loc)
                    visit2[moved_loc] = 1

        while queue2:
            loc = queue2.pop()
            tmp_loc = [loc - 1, loc + 1]

            for moved_loc in tmp_loc:
                if moved_loc >= N:
                    print(1)
                    exit()

                if 0 <= moved_loc < N:

                    if not visit2[moved_loc] and line2[moved_loc] == '1':
                        tmp_queue2.append(moved_loc)
                        visit2[moved_loc] = 1

            moved_loc = loc + k
            if moved_loc >= N:
                print(1)
                exit()

            if 0 <= moved_loc < N:
                if not visit1[moved_loc] and line1[moved_loc] == '1':
                    tmp_queue1.append(moved_loc)
                    visit1[moved_loc] = 1

        queue1 = tmp_queue1
        queue2 = tmp_queue2

    print(0)


if __name__ == '__main__':
    run()

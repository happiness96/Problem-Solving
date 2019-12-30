# -*- encoding: utf-8 -*-
import sys
from collections import deque
from copy import deepcopy
r_input = sys.stdin.readline


def run():
    # T: 테스트 케이스의 개수
    T = int(r_input())

    dx = [0, 0, 0, 1, -1]
    dy = [0, 1, -1, 0, 0]

    result = [list('...') for _ in range(3)]

    for _ in range(T):
        visit = []

        queue = deque([[list(r_input().rstrip()) for _ in range(3)]])

        visit.append(queue[0])
        cnt = 0
        flag = 0

        while True:
            for _ in range(len(queue)):
                tmp = queue.popleft()

                if tmp == result:
                    flag = 1
                    break

                for i in range(3):
                    for j in range(3):
                        save = deepcopy(tmp)

                        for k in range(5):
                            tmp_row = i + dx[k]
                            tmp_col = j + dy[k]

                            if 0 <= tmp_row < 3 and 0 <= tmp_col < 3:
                                if save[tmp_row][tmp_col] == '*':
                                    save[tmp_row][tmp_col] = '.'
                                else:
                                    save[tmp_row][tmp_col] = '*'

                        if save not in visit:
                            visit.append(save)
                            queue.append(save)

            if flag:
                print(cnt)
                break

            cnt += 1


run()

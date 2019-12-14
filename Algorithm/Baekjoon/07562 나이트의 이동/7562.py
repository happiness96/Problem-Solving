# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

T = int(r_input())          # 테스트 케이스의 개수

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, -2, 2, -2, 2, -1, 1]


def run():
    for _ in range(T):
        l = int(r_input())      # 체스판 한 변의 길이

        pre_loc = list(map(int, r_input().split()))     # 현재 나이트가 있는 칸
        tar_loc = list(map(int, r_input().split()))     # 나이트가 이동하려는 칸

        queue = [pre_loc]

        cnt = 0
        if tar_loc == pre_loc:
            print(cnt)
            continue

        cnt += 1

        visit = [[0] * l for _ in range(l)]
        visit[pre_loc[0]][pre_loc[1]] = 1

        while True:
            flag = 0
            tmp_queue = []

            while queue:
                loc = queue.pop()

                for i in range(8):
                    tmp_row = loc[0] + dx[i]
                    tmp_col = loc[1] + dy[i]

                    if 0 <= tmp_row < l and 0 <= tmp_col < l:
                        if not visit[tmp_row][tmp_col]:
                            if [tmp_row, tmp_col] == tar_loc:
                                print(cnt)
                                flag = 1
                                break

                            else:
                                tmp_queue.append([tmp_row, tmp_col])
                                visit[tmp_row][tmp_col] = 1

                if flag:
                    break

            if flag:
                break

            queue = tmp_queue
            cnt += 1


run()

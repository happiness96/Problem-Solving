# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline


def find_path(start_loc, destination):
    queue = deque([[start_loc, [start_loc]]])
    visit = [[0] * 8 for _ in range(8)]
    visit[start_x][start_y] = 1

    cnt = 0

    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]

    while queue:
        for _ in range(len(queue)):
            loc = queue.popleft()

            if loc[0] == destination:
                print(cnt, end=' ')

                for path in loc[1]:
                    print(chr(path[0] + 65), path[1] + 1, end=' ')

                return 0

            for k in range(4):
                for l in range(1, 5):
                    tmp_row = loc[0][0] + dx[k] * l
                    tmp_col = loc[0][1] + dy[k] * l

                    if 0 <= tmp_row < 8 and 0 <= tmp_col < 8:
                        if not visit[tmp_row][tmp_col]:
                            queue.append([(tmp_row, tmp_col), loc[1] + [(tmp_row, tmp_col)]])
                            visit[tmp_row][tmp_col] = 1

        cnt += 1

    return 1


if __name__ == '__main__':
    # 테스트 케이스의 개수
    T = int(r_input())

    for _ in range(T):
        start_x, start_y, end_x, end_y = map(str, r_input().rstrip().split())

        start_x = ord(start_x) - 65
        end_x = ord(end_x) - 65
        start_y = int(start_y) - 1
        end_y = int(end_y) - 1

        if (abs(start_x - end_x) + abs(start_y - end_y)) % 2:
            print('Impossible')
            continue

        start = (start_x, start_y)
        dest = (end_x, end_y)

        flag = find_path(start, dest)

        if flag:
            print('Impossible')

# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

if __name__ == '__main__':
    while True:
        L, R, C = map(int, r_input().split())

        start_loc = ()
        end_loc = ()

        if L == 0:
            break

        building = []

        for i in range(L):
            floor = []

            for j in range(R):
                line = list(r_input().rstrip())

                for k in range(C):
                    if line[k] == 'S':
                        start_loc = (i, j, k)

                    elif line[k] == 'E':
                        end_loc = (i, j, k)

                floor.append(line)

            building.append(floor)

            r_input()

        queue = deque([start_loc])
        minutes = 0

        visit = [[[0] * C for _ in range(R)] for _ in range(L)]
        visit[start_loc[0]][start_loc[1]][start_loc[2]] = 1

        dx = [0, 0, 1, -1, 0, 0]
        dy = [1, -1, 0, 0, 0, 0]
        dz = [0, 0, 0, 0, 1, -1]

        escaped = 0

        while queue and not escaped:
            for _ in range(len(queue)):
                loc = queue.popleft()

                if loc == end_loc:
                    print('Escaped in', minutes, 'minute(s).')
                    escaped = 1
                    break

                for k in range(6):
                    tmp_height = loc[0] + dx[k]
                    tmp_row = loc[1] + dy[k]
                    tmp_col = loc[2] + dz[k]

                    if 0 <= tmp_height < L and 0 <= tmp_row < R and 0 <= tmp_col < C:
                        if not visit[tmp_height][tmp_row][tmp_col] and building[tmp_height][tmp_row][tmp_col] in '.E':
                            visit[tmp_height][tmp_row][tmp_col] = 1
                            queue.append((tmp_height, tmp_row, tmp_col))

            minutes += 1

        if not escaped:
            print('Trapped!')

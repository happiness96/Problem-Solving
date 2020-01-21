# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

if __name__ == '__main__':
    board = [list(map(str, r_input().rstrip().split())) for _ in range(5)]
    visit = [[0] * 5 for _ in range(5)]
    case = set()

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(5):
        for j in range(5):
            queue = deque([(i, j, board[i][j])])

            for _ in range(5):
                for _ in range(len(queue)):
                    loc = queue.popleft()

                    for k in range(4):
                        tmp_row = loc[0] + dx[k]
                        tmp_col = loc[1] + dy[k]

                        if 0 <= tmp_row < 5 and 0 <= tmp_col < 5 and not visit[tmp_row][tmp_col]:
                            queue.append((tmp_row, tmp_col, loc[2] + board[tmp_row][tmp_col]))

            for q in queue:
                case.add(q[2])
    
    print(len(case))

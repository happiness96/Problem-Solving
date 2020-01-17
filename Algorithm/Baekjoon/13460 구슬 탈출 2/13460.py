# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline


def run():
    N, M = map(int, r_input().split())
    board = [list(r_input().rstrip()) for _ in range(N)]

    red_ball = []
    blue_ball = []

    visit = []

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                red_ball = [i, j]
                board[i][j] = '.'

            if board[i][j] == 'B':
                blue_ball = [i, j]
                board[i][j] = '.'

    visit.append([red_ball, blue_ball])

    queue = deque([[red_ball, blue_ball]])

    for co in range(1, 11):
        for _ in range(len(queue)):
            tmp = queue.popleft()

            red = tmp[0]
            blue = tmp[1]

            # move_left
            flag = 1
            tmp_b = 0
            for b_col in range(blue[1] - 1, -1, -1):
                if board[blue[0]][b_col] == 'O':
                    flag = 0
                    break
                if board[blue[0]][b_col] == '#':
                    tmp_b = b_col + 1
                    break

            if flag:
                tmp_r = 0
                for r_col in range(red[1] - 1, -1, -1):
                    if board[red[0]][r_col] == 'O':
                        print(co)
                        exit()

                    if board[red[0]][r_col] == '#':
                        tmp_r = r_col + 1
                        break

                v = [[red[0], tmp_r], [blue[0], tmp_b]]

                if v[0] == v[1]:
                    if red[1] > blue[1]:
                        v[0][1] += 1

                    else:
                        v[1][1] += 1

                if v not in visit:
                    visit.append(v)
                    queue.append(v)

            # move_right
            flag = 1
            tmp_b = 0
            for b_col in range(blue[1] + 1, M):
                if board[blue[0]][b_col] == 'O':
                    flag = 0
                    break
                if board[blue[0]][b_col] == '#':
                    tmp_b = b_col - 1
                    break

            if flag:
                tmp_r = 0
                for r_col in range(red[1] + 1, M):
                    if board[red[0]][r_col] == 'O':
                        print(co)
                        exit()

                    if board[red[0]][r_col] == '#':
                        tmp_r = r_col - 1
                        break

                v = [[red[0], tmp_r], [blue[0], tmp_b]]

                if v[0] == v[1]:
                    if red[1] > blue[1]:
                        v[1][1] -= 1

                    else:
                        v[0][1] -= 1

                if v not in visit:
                    visit.append(v)
                    queue.append(v)

            # move_up
            flag = 1
            tmp_b = 0
            for b_row in range(blue[0] - 1, -1, -1):
                if board[b_row][blue[1]] == 'O':
                    flag = 0
                    break
                if board[b_row][blue[1]] == '#':
                    tmp_b = b_row + 1
                    break

            if flag:
                tmp_r = 0
                for r_row in range(red[0] - 1, -1, -1):
                    if board[r_row][red[1]] == 'O':
                        print(co)
                        exit()

                    if board[r_row][red[1]] == '#':
                        tmp_r = r_row + 1
                        break

                v = [[tmp_r, red[1]], [tmp_b, blue[1]]]

                if v[0] == v[1]:
                    if red[0] > blue[0]:
                        v[0][0] += 1

                    else:
                        v[1][0] += 1

                if v not in visit:
                    visit.append(v)
                    queue.append(v)

            # move_down
            flag = 1
            tmp_b = 0
            for b_row in range(blue[0] + 1, N):
                if board[b_row][blue[1]] == 'O':
                    flag = 0
                    break
                if board[b_row][blue[1]] == '#':
                    tmp_b = b_row - 1
                    break

            if flag:
                tmp_r = 0
                for r_row in range(red[0] + 1, N):
                    if board[r_row][red[1]] == 'O':
                        print(co)
                        exit()

                    if board[r_row][red[1]] == '#':
                        tmp_r = r_row - 1
                        break

                v = [[tmp_r, red[1]], [tmp_b, blue[1]]]

                if v[0] == v[1]:
                    if red[0] > blue[0]:
                        v[1][0] -= 1

                    else:
                        v[0][0] -= 1

                if v not in visit:
                    visit.append(v)
                    queue.append(v)

    print(-1)


if __name__ == '__main__':
    run()

# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline
sys.setrecursionlimit(10**6)

puyo = {0: ['.']*8, 13: ['.']*8}           # 뿌요뿌요

for i in range(1, 13):
    s = r().rstrip()
    puyo[i] = ['.']

    for c in s:
        puyo[i].append(c)

    puyo[i].append('.')


def find_connection(r, c, color):           # 연결되어 있는지 확인하는 함수
    global connection

    if [r, c] in connection:
        return

    # print(connection)
    #
    # for t in puyo:
    #     print(''.join(puyo[t]))

    if 1 <= r <= 12 and 1 <= c <= 6:
        if puyo[r][c] == color:
            connection.append([r, c])
            find_connection(r - 1, c, color)
            find_connection(r + 1, c, color)
            find_connection(r, c - 1, color)
            find_connection(r, c + 1, color)


def next_round():           # 다음 라운드로 갈 경우
    global cnt

    for i in range(1, 7):
        remain = ''
        for j in range(1, 13):
            if puyo[j][i] != '.':
                remain += puyo[j][i]

        for j in range(1, 13-len(remain)):
            puyo[j][i] = '.'

        for j in range(1, 13-len(remain)):
            puyo[j][i] = '.'

        for j in range(len(remain)):
            puyo[j+13-len(remain)][i] = remain[j]

    cnt += 1


cnt = 0
while True:
    go_to_next_round = 0  # 다음 라운드로 갈지 결정

    for i in range(1, 13):
        for j in range(1, 7):
            if puyo[i][j] != '.':
                connection = []
                find_connection(i, j, puyo[i][j])

                if len(connection) > 3:
                    go_to_next_round = 1
                    for c in connection:
                        puyo[c[0]][c[1]] = '.'
                    break

    if not go_to_next_round:
        break

    next_round()

print(cnt)

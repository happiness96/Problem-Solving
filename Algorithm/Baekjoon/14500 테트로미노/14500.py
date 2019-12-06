import sys
r_input = sys.stdin.readline

# N: 세로 크기, M: 가로 크기
N, M = map(int, r_input().split())

board = [list(map(int, r_input().split())) for _ in range(N)]
result = 0

comp1 = N - 4
comp2 = M - 4
comp3 = N - 2
comp4 = M - 2
comp5 = N - 3
comp6 = M - 3

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def sero_line(row, col):        # 세로 작대기
    global result
    total = 0

    for r in range(row, row + 4):
        total += board[r][col]

    if total > result:
        result = total


def garo_line(row, col):        # 가로 작대기
    global result

    total = sum(board[row][col: col + 4])

    if total > result:
        result = total


def square(row, col):       # 사각형
    global result

    total = 0

    for k in range(4):
        total += board[row + dx[k]][col + dy[k]]

    if total > result:
        result = total


def block_3_1(row, col):
    global result

    tmp = 0

    for r in range(row, row + 3):
        tmp += board[r][col]

    if col > 0:
        for k in range(3):
            total = tmp + board[row + k][col - 1]

            if total > result:
                result = total

    if col < M - 1:
        for k in range(3):
            total = tmp + board[row + k][col + 1]

            if total > result:
                result = total


def block_1_3(row, col):
    global result

    tmp = sum(board[row][col: col + 3])

    if row > 0:
        for k in range(3):
            total = tmp + board[row - 1][col + k]

            if total > result:
                result = total

    if row < N - 1:
        for k in range(3):
            total = tmp + board[row + 1][col + k]

            if total > result:
                result = total


def block_2_2_1(row, col):
    global result
    tmp = board[row][col] + board[row][col + 1]

    if col > 0:
        total = tmp + board[row + 1][col - 1] + board[row + 1][col]

        if total > result:
            result = total

    if col < comp4:
        total = tmp + board[row + 1][col + 1] + board[row + 1][col + 2]

        if total > result:
            result = total


def block_2_2_2(row, col):
    global result

    tmp = board[row][col] + board[row + 1][col]

    if row > 0:
        total = tmp + board[row - 1][col + 1] + board[row][col + 1]

        if total > result:
            result = total

    if row < comp3:
        total = tmp + board[row + 1][col + 1] + board[row + 2][col + 1]

        if total > result:
            result = total


for i in range(N):
    for j in range(M):
        if i <= comp1:
            sero_line(i, j)

        if j <= comp2:
            garo_line(i, j)

        if i <= comp3 and j <= comp4:
            square(i, j)

        if i <= comp5:
            block_3_1(i, j)

        if j <= comp6:
            block_1_3(i, j)

        if i <= comp3 and j <= comp4:
            block_2_2_1(i, j)
            block_2_2_2(i, j)

print(result)

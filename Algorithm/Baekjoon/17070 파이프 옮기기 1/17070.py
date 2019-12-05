import sys
r_input = sys.stdin.readline

N = int(r_input())      # 집의 크기
board = [list(map(int, r_input().split())) for _ in range(N)]       # 집
cnt = 0
stack = [[0, 1, 0]]


def chk_wall(r, c, m):          # 벽 체크
    if m == 0 or m == 2:
        return not board[r][c]

    else:
        return not (board[r][c] or board[r-1][c] or board[r][c-1])


f = N - 1

while stack:
    tmp = stack.pop()

    if tmp[0] == tmp[1] == f:
        cnt += 1
        continue

    tmp_row = tmp[0] + 1
    tmp_col = tmp[1] + 1
    mode = tmp[2]

    if mode == 0:
        if tmp_col < N:
            if chk_wall(tmp[0], tmp_col, 0):
                stack.append([tmp[0], tmp_col, 0])

        if tmp_row < N and tmp_col < N:
            if chk_wall(tmp_row, tmp_col, 1):
                stack.append([tmp_row, tmp_col, 1])

    elif mode == 1:
        if tmp_col < N:
            if chk_wall(tmp[0], tmp_col, 0):
                stack.append([tmp[0], tmp_col, 0])

        if tmp_row < N:
            if chk_wall(tmp_row, tmp[1], 2):
                stack.append([tmp_row, tmp[1], 2])

        if tmp_row < N and tmp_col < N:
            if chk_wall(tmp_row, tmp_col, 1):
                stack.append([tmp_row, tmp_col, 1])

    else:
        if tmp_row < N:
            if chk_wall(tmp_row, tmp[1], 2):
                stack.append([tmp_row, tmp[1], 2])

        if tmp_row < N and tmp_col < N:
            if chk_wall(tmp_row, tmp_col, 1):
                stack.append([tmp_row, tmp_col, 1])

print(cnt)

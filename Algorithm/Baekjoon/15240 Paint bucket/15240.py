import sys
r_input = sys.stdin.readline


def run():
    R, C = map(int, r_input().split())

    grid = [list(r_input().rstrip()) for _ in range(R)]

    r, c, f = map(int, r_input().split())
    f = str(f)

    stack = {(r, c)}
    num = grid[r][c]
    grid[r][c] = f

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while stack:
        loc = stack.pop()

        for i in range(4):
            tmp_row = loc[0] + dx[i]
            tmp_col = loc[1] + dy[i]

            if 0 <= tmp_row < R and 0 <= tmp_col < C:
                if grid[tmp_row][tmp_col] == num:
                    stack.add((tmp_row, tmp_col))
                    grid[tmp_row][tmp_col] = f

    for g in grid:
        print(''.join(g))


run()

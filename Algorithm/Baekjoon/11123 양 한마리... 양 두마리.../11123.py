import sys
r_input = sys.stdin.readline


def run():
    T = int(r_input())      # 테스트 케이스의 개수

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for _ in range(T):
        # H: 그리드의 높이, W: 그리드의 너비
        H, W = map(int, r_input().split())

        grid = []

        for _ in range(H):
            grid.append(list(r_input().rstrip()))

        cnt = 0

        # BFS
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '#':
                    stack = {(i, j)}
                    grid[i][j] = '.'

                    while stack:
                        loc = stack.pop()

                        for k in range(4):
                            tmp_row = loc[0] + dx[k]
                            tmp_col = loc[1] + dy[k]

                            if 0 <= tmp_row < H and 0 <= tmp_col < W:
                                if grid[tmp_row][tmp_col] == '#':
                                    grid[tmp_row][tmp_col] = '.'
                                    stack.add((tmp_row, tmp_col))

                    cnt += 1

        print(cnt)


run()

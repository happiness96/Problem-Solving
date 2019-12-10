import sys
r_input = sys.stdin.readline

M, N = map(int, r_input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

grid = {}
visit = [[0] * N for _ in range(M)]

comp = M - 1

for i in range(M):
    grid[i] = list(r_input().rstrip())


def run(col):
    stack = {(0, col)}

    while stack:
        loc = stack.pop()
        visit[loc[0]][loc[1]] = 1

        for i in range(4):
            tmp_row = loc[0] + dx[i]
            tmp_col = loc[1] + dy[i]

            if 0 <= tmp_row < M and 0 <= tmp_col < N:
                if not visit[tmp_row][tmp_col]:
                    if grid[tmp_row][tmp_col] == '0':
                        if tmp_row == M - 1:
                            print('YES')
                            exit()
                        if tmp_row == 0:
                            chk[tmp_col] = 1
                        visit[tmp_row][tmp_col] = 1
                        stack.add((tmp_row, tmp_col))


chk = [0 for _ in range(N)]
for c in range(N):
    if grid[0][c] == '0' and not chk[c]:
        if not visit[0][c]:
            run(c)

print('NO')

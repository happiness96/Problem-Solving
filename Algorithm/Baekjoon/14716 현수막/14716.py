import sys
r_input = sys.stdin.readline

M, N = map(int, r_input().split())

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

banner = {i: list(map(int, r_input().split())) for i in range(M)}
cnt = 0

for i in range(M):
    for j in range(N):
        if banner[i][j]:
            stack = [[i, j]]
            banner[i][j] = 0

            while stack:
                loc = stack.pop()

                for k in range(8):
                    tmp_x = loc[0] + dx[k]
                    tmp_y = loc[1] + dy[k]

                    if 0 <= tmp_x < M and 0 <= tmp_y < N:
                        if banner[tmp_x][tmp_y]:
                            banner[tmp_x][tmp_y] = 0
                            stack.append([tmp_x, tmp_y])

            cnt += 1

print(cnt)

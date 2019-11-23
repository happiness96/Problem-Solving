# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 세로 크기, M: 가로 크기
N, M = map(int, r_input().split())

# r, c: 현재 로봇 청소기의 위치
# d: 로봇 청소기가 바라보고 있는 방향 (0 = 북쪽, 1 = 동쪽, 2 = 남쪽, 3 = 서쪽)
r, c, d = map(int, r_input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

room = {}
cleaned = {}

for i in range(N):
    room[i] = list(map(int, r_input().split()))
    cleaned[i] = [0] * M

cnt = 0         # 로봇 청소기가 청소하는 칸의 개수
back = 0        # 후진

while True:
    # 현재 위치를 청소한다
    cleaned[r][c] = 1
    if back:
        back = 0
    else:
        cnt += 1

    # 네 방향 검사
    flag = 1            # 네 방향 모두 청소가 되었으면 1
    for i in range(4):
        tmp_r = r + dx[i]
        tmp_c = c + dy[i]

        if 0 <= tmp_r < N and 0 <= tmp_c < M:
            if not room[tmp_r][tmp_c] and not cleaned[tmp_r][tmp_c]:
                flag = 0
                break

    # 네방향 모두 청소가 된 경우
    if flag:
        if d == 0:
            r += 1
            if r == N or room[r][c]:
                break
            else:
                back = 1
                continue

        elif d == 1:
            c -= 1
            if c == -1 or room[r][c]:
                break
            else:
                back = 1
                continue

        elif d == 2:
            r -= 1
            if r == -1 or room[r][c]:
                break
            else:
                back = 1
                continue

        else:
            c += 1
            if c == M or room[r][c]:
                break
            else:
                back = 1
                continue

    # 아직 청소할 공간이 존재한다면
    for i in range(4):
        d -= 1
        if d < 0:
            d = 3

        if d == 0:
            if r > 0 and not room[r - 1][c] and not cleaned[r - 1][c]:
                r -= 1
                break

        elif d == 1:
            if c < M - 1 and not room[r][c + 1] and not cleaned[r][c + 1]:
                c += 1
                break

        elif d == 2:
            if r < N - 1 and not room[r + 1][c] and not cleaned[r + 1][c]:
                r += 1
                break

        else:
            if c > 0 and not room[r][c - 1] and not cleaned[r][c - 1]:
                c -= 1
                break

print(cnt)

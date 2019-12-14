# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

s = r_input().rstrip()
ori = [ord(s[0]) - 64, int(s[1])]

visit = [[0] * 7 for _ in range(7)]
visit[ori[0]][ori[1]] = 1

pre_loc = ori

flag = 1

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]


def chk_move(pre, aft):
    for i in range(8):
        if [pre[0] + dx[i], pre[1] + dy[i]] == aft:
            return 1

    return 0


for _ in range(35):
    v = r_input().rstrip()

    if not flag:
        continue

    aft_loc = [ord(v[0]) - 64, int(v[1])]

    if visit[aft_loc[0]][aft_loc[1]]:
        flag = 0
        continue

    visit[aft_loc[0]][aft_loc[1]] = 1

    flag = chk_move(pre_loc, aft_loc)

    pre_loc = aft_loc

if flag:
    flag = chk_move(pre_loc, ori)

print('Valid' if flag else 'Invalid')

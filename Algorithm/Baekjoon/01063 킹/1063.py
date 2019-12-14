# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 킹의 위치, 돌의 위치, 킹이 움직이는 횟수
king, rock, N = map(str, r_input().rstrip().split())

N = int(N)


def find_location(loc):
    return [ord(loc[0]) - 64, int(loc[1])]


def move(r_m, c_m):
    king_loc[0] += r_m
    king_loc[1] += c_m

    if 0 in king_loc or 9 in king_loc:
        king_loc[0] -= r_m
        king_loc[1] -= c_m
        return

    if king_loc == rock_loc:
        rock_loc[0] += r_m
        rock_loc[1] += c_m

        if 0 in rock_loc or 9 in rock_loc:
            rock_loc[0] -= r_m
            rock_loc[1] -= c_m
            king_loc[0] -= r_m
            king_loc[1] -= c_m


king_loc = find_location(king)
rock_loc = find_location(rock)

for _ in range(N):
    order = r_input().rstrip()      # 움직이는 정보

    mx = -order.count('L') + order.count('R')
    my = -order.count('B') + order.count('T')

    move(mx, my)

print(chr(king_loc[0] + 64) + str(king_loc[1]))
print(chr(rock_loc[0] + 64) + str(rock_loc[1]))

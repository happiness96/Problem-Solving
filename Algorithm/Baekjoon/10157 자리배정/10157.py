# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

C, R = map(int, r_input().split())
K = int(r_input())

s_x = 1
s_y = 1

tmp = 1

if K > C * R:
    print(0)
    exit()

for i in range(min((C + 1) // 2, (R + 1) // 2)):
    tmp2 = tmp + (R - 1) + (C - 1) + (R - 1) + (C - 2)

    if tmp <= K <= tmp2:
        break

    C -= 2
    R -= 2

    s_x += 1
    s_y += 1

    tmp = tmp2 + 1

if tmp <= K <= tmp + (R - 1):
    print(s_x, s_y + K - tmp)
    exit()

tmp += R
s_x += 1
s_y += (R - 1)

if tmp <= K <= tmp + (C-2):
    print(s_x + K - tmp, s_y)
    exit()

tmp += (C - 1)
s_x += (C - 2)
s_y -= 1

if tmp <= K <= tmp + (R - 2):
    print(s_x, s_y - (K - tmp))
    exit()

tmp += (R - 1)
s_x -= 1
s_y -= (R - 2)

print(s_x - (K - tmp), s_y)

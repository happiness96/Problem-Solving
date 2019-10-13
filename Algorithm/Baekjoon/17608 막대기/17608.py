#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # 막대기의 개수

sticks = []         # 막대들의 길이
cnt = 0             # 오른쪽에서 보이는 막대의 수

for i in range(N):
    sticks.append(int(r()))

highst = 0          # 보는 방향에서 가장 높은 막대 길이

for stick in sticks[::-1]:
    if stick > highst:
        highst = stick
        cnt += 1

print(cnt)

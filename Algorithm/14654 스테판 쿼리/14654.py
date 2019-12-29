# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 라운드의 수
N = int(r_input())
team1 = list(map(int, r_input().split()))
team2 = list(map(int, r_input().split()))

result = 0

flag = 0
cnt = 0

win = [(2, 1), (3, 2), (1, 3)]

for i in range(N):
    if (team1[i], team2[i]) in win:
        if flag == 1:
            cnt += 1
        else:
            flag = 1
            cnt = 1

    elif (team2[i], team1[i]) in win:
        if flag == 2:
            cnt += 1
        else:
            flag = 2
            cnt = 1

    else:
        if flag == 1:
            flag = 2

        else:
            flag = 1

        cnt = 1

    result = max(result, cnt)

print(result)

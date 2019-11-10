# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

R, C = map(int, r_input().split())          # 목장의 크기

farm = {0: '.'*(C+2), R+1: '.'*(C+2)}       # 목장의 상태

for i in range(1, R+1):
    farm[i] = '.' + r_input().rstrip() + '.'

for i in range(1, R+1):
    for j in range(1, C+1):

        if farm[i][j] == 'S':
            temp = [farm[i-1][j], farm[i+1][j], farm[i][j-1], farm[i][j+1]]

            if 'W' in temp:             # 양과 늑대가 붙어있는 경우
                print(0)
                exit()

print(1)
for i in range(1, R+1):
    print(farm[i][1:-1].replace('.', 'D'))

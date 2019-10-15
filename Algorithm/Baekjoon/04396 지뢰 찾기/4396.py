#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

n = int(r())        # 격자의 크기

mine = {0:'.'*(n+2), n+1:'.'*(n+2)}     # 지뢰 밭

for i in range(1, n+1):
    mine[i] = '.' + r().rstrip() + '.'

check = {}
for i in range(1, n+1):
    check[i] = '.' + r().rstrip() + '.'

game_over = 0

for i in range(1, n+1):         # 열린 칸에 지뢰가 있는지 체크
    for j in range(1, n+1):
        if check[i][j] == 'x' and mine[i][j] == '*':
            game_over = 1
            break

for i in range(1, n+1):
    for j in range(1, n+1):
        if game_over and mine[i][j] == '*':
            print('*', end='')
            
        elif check[i][j] == '.':      # 아직 열리지 않은 칸
            print('.', end='')
            
        elif check[i][j] == 'x':        # 열린 칸
            cnt = 0
            for k in range(i-1, i+2):
                for h in range(j-1, j+2):
                    if mine[k][h] == '*':
                        cnt += 1
            print(cnt, end='')
    print()

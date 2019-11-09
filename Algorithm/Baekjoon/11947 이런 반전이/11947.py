# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

T = int(r_input())          # 테스트 케이스의 개수

for _ in range(T):
    N = r_input().rstrip()          # 양의 정수
    mult = ''                       # 곱할 수

    if int(N[0]) >= 5:
        N = '5' + '0' * (len(N) - 1)

    for i in range(len(N)):
        mult += str(9 - int(N[i]))
    
    print(int(N) * int(mult))

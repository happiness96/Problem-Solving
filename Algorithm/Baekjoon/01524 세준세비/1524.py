# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

T = int(r_input())          # 테스트 케이스의 개수
r_input()

for _ in range(T):
    N, M = map(int, r_input().split())              # 세준이는 N명의 병사, 세비는 M명의 병사

    sejun = max(map(int, r_input().split()))
    sebi = max(map(int, r_input().split()))

    print('S' if sejun >= sebi else 'B')
    r_input()

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

T = int(r_input())      # 테스트 케이스의 개수

for _ in range(T):
    s1, s2 = map(str, r_input().rstrip().split())

    print('Distances: ', end='')

    for i in range(len(s1)):
        dist = ord(s2[i]) - ord(s1[i])
        print(26 + dist if dist < 0 else dist, end=' ')
        
    print()

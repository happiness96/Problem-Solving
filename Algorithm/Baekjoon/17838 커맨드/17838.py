# -*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # 테스트 케이스의 개수

for i in range(T):
    S = r().rstrip()

    if len(S) != 7:
        print(0)
        continue

    if S[0] == S[1] == S[4] and S[2] == S[3] == S[5] == S[6] and S[0] != S[2]:
        print(1)

    else:
        print(0)

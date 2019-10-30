#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # 문자열의 길이
S = r().rstrip()

lever = [0,0,0]     # 레버를 당긴 횟수
abc = 0         # 구역을 나타냄(0: A구역, 1: B구역, 2: C구역)

if S.count('W') < 2:        # C구역까지 광차가 이동하지 않은 경우
    print(0)
    exit()

for i in range(N):
    if S[i] == 'W':         # 구역을 넘어가는 경우
        abc = min(2, abc+1)
    else:                   # 레버를 당기는 경우
        lever[abc] += 1

if lever[1] > 0:        # 멀티트랙 드리프팅 현상 발생
    print(6)

else:
    print(1 if lever[0] % 2 else 5)

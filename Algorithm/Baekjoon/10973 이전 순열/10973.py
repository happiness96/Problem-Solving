#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # N: 숫자의 개수
permu = list(map(int, r().split()))         # 주어진 순열

is_minus = 1
for i in range(1, N+1):
    if permu[i-1] != i:
        is_minus = 0

if is_minus:        # 내림차순으로 이루어진 수열일 경우
    print(-1)
    exit()


ind = 0
for i in range(N):            # 나머지의 경우 뒷자리의 숫자보다 앞자리의 숫자가 큰 경우를 탐색
    if permu[N-i-1] < permu[N-i-2]:
        ind = N-i-2
        break

for i in range(ind):
    print(permu[i], end=' ')

temp = sorted(permu[ind:], reverse = True)
t = temp.index(permu[ind]) + 1

print(temp[t], end=' ')

temp.pop(t)

for i in temp:
    print(i, end=' ')

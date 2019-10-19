#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # 수의 개수
permu = list(map(int,r().split()))      # 주어진 순열

is_reversed = 1
for i in range(1, N+1):
    if i != permu[N-i]:
        is_reversed = 0

if is_reversed:         # 주어진 순열 다음이 없을 경우
    print(-1)
    exit()

if permu[-1] > permu[-2]:       # 맨 끝의 숫자가 그 앞자리 숫자보다 큰 경우
    for num in permu[:-2]:
        print(num, end=' ')
    print(permu[-1], permu[-2])
    exit()


ind = 0
for i in range(N-1):            # 나머지의 경우 뒷자리의 숫자보다 앞자리의 숫자가 작은 경우를 탐색
    if permu[N-2-i] < permu[N-1-i]:
        ind = N-i-2
        break

for i in range(ind):
    print(permu[i], end=' ')
    
temp = sorted(permu[ind:])
t = temp.index(permu[ind]) + 1

print(temp[t], end=' ')

temp.pop(t)

for i in temp:
    print(i, end=' ')

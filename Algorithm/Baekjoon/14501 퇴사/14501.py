#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())            # 기간

consult = {}
result = []

for i in range(1, N+1):         # 상담했을 때 받을 수 있는 수당과 걸리는 기간
    consult[i] = list(map(int,r().split()))


def consulting(day, T, earned):     # DFS 방식
    if day + T > N + 1:
        result.append(earned)
        return
    
    if day + T == N + 1:
        result.append(earned + consult[day][1])
        return
    
    for i in range(day + T, N+1):
        consulting(i, consult[i][0], earned + consult[day][1])


for i in range(1, N+1):
    consulting(i, consult[i][0], 0)

print(max(result))

#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())            # N: 구슬의 개수
W = list(map(int,r().split()))      # 각 에너지 구슬의 무게

result = []


def get_energy(node, energy):       # DFS 방식, 에너지 수집
    energy += W[node-1] * W[node + 1]
    temp = W.pop(node)
    
    if len(W) == 2:     # 더이상 뺄 구슬이 없으면
        result.append(energy)
    else:
        for i in range(1, len(W)-1):
            get_energy(i, energy)
    
    W.insert(node, temp)


for i in range(1, N-1):
    get_energy(i, 0)

print(max(result))

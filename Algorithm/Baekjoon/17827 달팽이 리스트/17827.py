# -*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N, M, V = map(int, r().split())     # N: 노드의 개수, M: 질문의 횟수, V: N번 노드가 가리키는 노드의 번호
nodes = list(map(int, r().split()))

for i in range(M):
    K = int(r())

    if K < N:
        print(nodes[K])
        continue

    K -= N
    rot = N - V + 1     # 순회를 이루는 노드들의 개수
    K %= rot
    K += V - 1

    print(nodes[K])

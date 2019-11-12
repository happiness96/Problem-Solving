# -*- encoding: utf-8 -*-
import sys
import heapq
r_input = sys.stdin.readline

# N명의 학생들을 키 순서대로 줄을 세우려한다.
# M회 키를 비교한다.
N, M = map(int, r_input().split())
line = [0] * (N+1)          # line의 인덱스의 번호를 가진 학생보다 앞에 출력해야하는 학생 수
students = {}

for i in range(M):
    # 학생 A가 B보다 앞에 있어야 한다.
    A, B = map(int, r_input().split())

    line[B] += 1

    if A in students:
        students[A].append(B)

    else:
        students[A] = [B]

queue = []

# 위상 정렬
for i in range(1, N+1):           # 다른 학생의 뒤에 나올 조건이 없는 학생들 먼저 heap에 삽입 (간선이 0인 학생)
    if not line[i]:
        heapq.heappush(queue, i)

while queue:
    temp1 = heapq.heappop(queue)
    print(temp1, end=' ')

    if temp1 in students:
        for t in students[temp1]:
            line[t] -= 1

            if not line[t]:
                heapq.heappush(queue, t)

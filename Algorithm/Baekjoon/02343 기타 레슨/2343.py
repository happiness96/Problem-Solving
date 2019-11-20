# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())      # N: 레슨의 수, M: 블루레이의 개수
lesson = list(map(int, r_input().split()))          # 각 레슨의 길이

A = 0
B = sum(lesson)

result = B

if M == 1:
    print(B)
    exit()

if N == M:
    print(max(lesson))
    exit()

pre = B

while True:                 # 이분 탐색
    cmp = (A + B) // 2

    if pre == cmp:
        break

    total = 0
    fail = 0

    stack = []

    for i in range(N):
        total += lesson[i]

        if total == cmp:
            stack.append(total)
            total = 0
            continue

        elif total > cmp:
            stack.append(total - lesson[i])
            total = lesson[i]

        if i == N-1:
            stack.append(total)

    if max(stack) > cmp or len(stack) > M:
        A = cmp

    else:
        B = cmp
        result = min(result, cmp)

    pre = cmp

print(result)

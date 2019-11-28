# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N개의 책이 있다, 세준이가 한 번에 들 수 있는 책의 개수는 M이다.
N, M = map(int, r_input().split())

minus = []      # 음의 위치
plus = []       # 양의 위치

for c in map(int, r_input().split()):
    if c < 0:
        minus.append(-c)
    else:
        plus.append(c)

minus.sort()
plus.sort()

loc = 0         # 현재 위치
result = 0      # 총 이동 거리

tmp = 0

if plus and not minus:
    tmp = plus[-1]
    for _ in range(M):
        if plus:
            plus.pop()

elif minus and not plus:
    tmp = minus[-1]
    for _ in range(M):
        if minus:
            minus.pop()
else:
    if plus[-1] >= minus[-1]:
        tmp = plus[-1]
        for _ in range(M):
            if plus:
                plus.pop()
    else:
        tmp = minus[-1]
        for _ in range(M):
            if minus:
                minus.pop()

while plus or minus:
    if plus and not minus:
        result += 2 * plus[-1]
        for _ in range(M):
            if plus:
                plus.pop()

    elif minus and not plus:
        result += 2 * minus[-1]
        for _ in range(M):
            if minus:
                minus.pop()

    else:
        if plus[-1] >= minus[-1]:
            result += 2 * plus[-1]
            for _ in range(M):
                if plus:
                    plus.pop()

        else:
            result += 2 * minus[-1]
            for _ in range(M):
                if minus:
                    minus.pop()

print(result + tmp)

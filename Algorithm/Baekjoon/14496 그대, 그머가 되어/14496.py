# -*- encoding: utf-8 -*-
import sys
from collections import deque

r = sys.stdin.readline
sys.setrecursionlimit(10**8)

a, b = map(int, r().split())        # 머호가 바꾸려는 문자
N, M = map(int, r().split())        # N: 전체 문자의 수, M: 치환 가능한 문자의 수

connection = {}                     # 연결 고리

for i in range(M):
    num1, num2 = map(int, r().split())

    if num1 in connection:
        if num2 not in connection[num1]:
            connection[num1].append(num2)

    else:
        connection[num1] = [num2]

    if num2 in connection:
        if num1 not in connection[num2]:
            connection[num2].append(num1)

    else:
        connection[num2] = [num1]


def find_result(next_search, cnt):          # 다음 탐색 찾기 (BFS)
    if b in next_search:
        print(cnt)
        exit()

    temp = deque()

    while next_search:
        t = next_search.pop()

        if t in connection:
            for num in connection[t]:
                if num not in temp:
                    temp.append(num)

            connection.pop(t)

    if temp:
        find_result(temp, cnt + 1)


find_result([a], 0)
print(-1)

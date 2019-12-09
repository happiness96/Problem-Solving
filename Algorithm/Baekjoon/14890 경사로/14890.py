# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, L = map(int, r_input().split())

result = 0
stack = []


def chk_road(line):         # 지나갈 수 있는 길인지 검사
    height = line[0]
    check = [0] * N

    for i in range(1, N):
        if line[i] == height:
            continue

        elif line[i] - height == 1:
            if i < L:
                return 0

            for j in range(i - 1, i - L - 1, -1):
                if line[j] != height:
                    return 0

                if check[j]:
                    return 0

                check[j] = 1

            height = line[i]

        elif line[i] - height == -1:
            if i > N - L:
                return 0

            for j in range(i, i + L):
                if line[j] != line[i]:
                    return 0

                if check[j]:
                    return 0

                check[j] = 1

            height = line[i]

        else:
            return 0
    
    return 1


for _ in range(N):
    stack.append(list(map(int, r_input().split())))
    result += chk_road(stack[-1])

for j in range(N):
    tmp = []

    for i in range(N):
        tmp.append(stack[i][j])

    result += chk_road(tmp)

print(result)

# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# N x N 크기의 땅이 있고, 인접한 두 나라의 인구 차가 L 이상 R 이하라면 국경선을 연다.
N, L, R = map(int, r_input().split())
result = 0              # 인구 이동 횟수

population = {}         # 각 나라의 인구 수

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    population[i] = list(map(int, r_input().split()))

while True:
    chk = [[0] * N for _ in range(N)]
    summation = {}
    ind = 1

    for i in range(N):
        for j in range(N):

            if not chk[i][j]:
                summation[ind] = [0, 0]
                stack = deque()

                if j != N-1:
                    if L <= abs(population[i][j] - population[i][j+1]) <= R:
                        stack.append([i, j])
                        stack.append([i, j+1])

                        chk[i][j] = ind
                        chk[i][j+1] = ind

                if i != N - 1:
                    if L <= abs(population[i][j] - population[i + 1][j]) <= R:
                        if [i, j] not in stack:
                            stack.append([i, j])

                        stack.append([i + 1, j])

                        chk[i][j] = ind
                        chk[i + 1][j] = ind

                flag = 0

                if stack:
                    flag = 1

                while stack:
                    loc = stack.popleft()

                    summation[ind][0] += population[loc[0]][loc[1]]
                    summation[ind][1] += 1

                    for k in range(4):
                        row = loc[0] + dx[k]
                        col = loc[1] + dy[k]

                        if 0 <= row < N and 0 <= col < N:
                            if not chk[row][col] and L <= abs(population[loc[0]][loc[1]] - population[row][col]) <= R:
                                chk[row][col] = ind
                                stack.append([row, col])

                if flag:
                    ind += 1

    if ind == 1:
        break

    temp = [0]
    for i in range(1, ind):
        temp.append(summation[i][0] // summation[i][1])

    for i in range(N):
        for j in range(N):
            if chk[i][j]:
                population[i][j] = temp[chk[i][j]]

    result += 1

print(result)

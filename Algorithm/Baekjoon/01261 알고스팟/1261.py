# -*- encoding: utf-8 -*-
import sys
import heapq
r_input = sys.stdin.readline

N, M = map(int, r_input().split())        # 미로의 크기

maze = {}
cost = {}

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

for i in range(M):
    maze[i] = []

    for c in r_input().rstrip():
        maze[i].append(int(c))

    cost[i] = ['INF'] * N

cost[0][0] = 0

if M == 1:
    print(maze[0].count(1))
    exit()

if N == 1:
    total = 0
    for i in range(M):
        total += maze[i][0]
    print(total)
    exit()

queue = []

for i in range(2):
    heapq.heappush(queue, (maze[dx[i]][dy[i]], dx[i], dy[i]))
    cost[dx[i]][dy[i]] = maze[dx[i]][dy[i]]


def dijkstra():
    while queue:
        mini = heapq.heappop(queue)
        min_cost = mini[0]
        min_x = mini[1]
        min_y = mini[2]

        for i in range(4):
            tmp_x = min_x + dx[i]
            tmp_y = min_y + dy[i]

            if 0 <= tmp_x < M and 0 <= tmp_y < N:
                tmp_cost = min_cost + maze[tmp_x][tmp_y]

                if cost[tmp_x][tmp_y] == 'INF' or tmp_cost < cost[tmp_x][tmp_y]:
                    cost[tmp_x][tmp_y] = tmp_cost
                    heapq.heappush(queue, (tmp_cost, tmp_x, tmp_y))


dijkstra()

print(cost[M-1][N-1])

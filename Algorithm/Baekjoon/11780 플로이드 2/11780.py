# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def floyd():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                tmp = cost[j][i] + cost[i][k]

                if tmp < cost[j][k]:
                    way[j][k] = [j, i, k]
                    cost[j][k] = tmp


def find_way(row, col):
    length = len(way[row][col])

    if length == 2:
        return [row, col]

    way_l = [row]

    for i in range(1, len(way[row][col])):
        way_l.extend(find_way(way[row][col][i - 1], way[row][col][i]))

    way_l.append(col)

    return way_l


if __name__ == '__main__':
    n = int(r_input())      # 도시의 개수
    m = int(r_input())      # 버스의 개수

    INF = sys.maxsize

    cost = [[INF] * (n + 1) for _ in range(n + 1)]
    way = [[[]] * (n + 1) for _ in range(n + 1)]

    for i in range(m):
        # a에서 b로 가는 버스, 비용 c
        a, b, c = map(int, r_input().split())

        if cost[a][b] == INF:
            cost[a][b] = c
            way[a][b] = [a, b]

        else:
            if c < cost[a][b]:
                cost[a][b] = c
                way[a][b] = [a, b]

    floyd()

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(0 if i == j or cost[i][j] == INF else cost[i][j], end=' ')
        print()

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j or not way[i][j]:
                print(0)
            else:
                result = find_way(i, j)
                real_result = [result[0]]

                for k in range(1, len(result)):
                    if result[k] != result[k - 1]:
                        real_result.append(result[k])

                print(len(real_result), *real_result)

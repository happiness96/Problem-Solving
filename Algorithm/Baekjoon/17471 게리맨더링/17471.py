# -*- encoding: utf-8 -*-
import sys
from itertools import combinations
r = sys.stdin.readline

N = int(r())            # 구역의 수
people = list(map(int, r().split()))        # 각 구역의 사람 수
connection ={}      # 각 구역의 인점한 구역 번호
result = []

for i in range(1, N+1):
    temp = list(map(int, r().split()))
    if len(temp) == 1:
        connection[i] = [0]

    else:
        connection[i] = temp[1:]


def find_connection(con):           # 선거구끼리 연결되어 있는지 확인
    connect = [con[0]]

    more = [con[0]]
    while more:
        tmp = more.pop()
        if tmp == 0:
            continue
        for c in connection[tmp]:
            if not c in connect and c in con:
                more.append(c)
            connect.append(c)

    for c in con:
        if not c in connect:
            return 0

    return 1


area = list(connection.keys())      # 지역 번호

for cnt in range(1, N):         # 첫 번째 선거구의 구역 수
    for first in combinations(area, cnt):
        if first[0] != 1:
            break

        second = []
        for i in range(1, N+1):
            if not i in first:
                second.append(i)

        ok = find_connection(list(first))

        if not ok:          # 하나라도 떨어져있는 경우
            continue

        ok = find_connection(second)

        if not ok:
            continue

        sum_first = 0           # 첫 번째 구역의 인원 총합
        sum_second = 0          # 두 번째 구역의 인원 총합

        for t in first:
            sum_first += people[t-1]

        for t in second:
            sum_second += people[t-1]

        result.append(abs(sum_first - sum_second))

print(min(result) if result else -1)

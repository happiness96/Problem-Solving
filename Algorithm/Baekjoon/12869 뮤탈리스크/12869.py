# -*- encoding: utf-8 -*-
import sys
from collections import deque
from itertools import permutations
r_input = sys.stdin.readline

# N: SCV의 수
N = int(r_input())

# SCV의 초기 체력
scv = list(map(int, r_input().split()))
queue = deque([scv])

if N == 1:
    result = scv[0] // 9
    if scv[0] % 9:
        result += 1

elif N == 2:
    cnt = 1

    flag = 1

    while flag:
        for _ in range(len(queue)):
            tmp = queue.popleft()
            a = max(tmp[0] - 9, 0)
            b = max(tmp[1] - 3, 0)

            if a == b == 0:
                result = cnt
                flag = 0
                break

            queue.append([a, b])

            a = max(tmp[1] - 9, 0)
            b = max(tmp[0] - 3, 0)

            if a == b == 0:
                result = cnt
                flag = 0
                break

            queue.append([b, a])
        cnt += 1

else:
    save = [9, 3, 1]
    cnt = 1

    flag = 1

    while flag:
        tmp_queue = deque()
        for _ in range(len(queue)):
            tmp = queue.popleft()

            for case in permutations([0, 1, 2], 3):
                a = max(tmp[0] - save[case[0]], 0)
                b = max(tmp[1] - save[case[1]], 0)
                c = max(tmp[2] - save[case[2]], 0)

                if a == b == c == 0:
                    print(cnt)
                    exit()
                z = sorted([a, b, c])

                if z not in tmp_queue:
                    tmp_queue.append(z)
        queue = tmp_queue
        cnt += 1

print(result)

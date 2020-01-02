# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# n: 회사의 직원 수, m: 최초의 갈굼 횟수
n, m = map(int, r_input().split())
master = {num: [] for num in range(1, n + 1)}
result = [0] * (n + 1)

tmp = [0] + list(map(int, r_input().split()))

for a in range(2, n + 1):
    master[tmp[a]].append(a)

crave = [0] * (n + 1)

for _ in range(m):
    # i: 갈굼을 당한 직원 번호, w: 갈굼의 수치
    i, w = map(int, r_input().split())
    crave[i] += w

for i in range(n + 1):
    w = crave[i]
    if w:
        queue = [i]

        while queue:
            num = queue.pop()
            result[num] += w
            queue.extend(master[num])

print(*result[1:])

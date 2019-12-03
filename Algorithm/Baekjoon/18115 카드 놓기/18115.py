import sys
from collections import deque
r_input = sys.stdin.readline

N = int(r_input())

A = list(map(int, r_input().split()))
result = deque()


def one(n):
    result.extendleft([str(n)])


def two(n):
    tmp = [str(n)]
    tmp.append(result.popleft())
    result.extendleft(tmp)


def three(n):
    result.extend([str(n)])


for i in range(1, N + 1):
    num = A.pop()

    if num == 1:
        one(i)
        continue

    if num == 2:
        two(i)
        continue

    three(i)

print(' '.join(result))

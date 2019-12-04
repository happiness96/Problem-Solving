import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())

stack = []

for _ in range(M):
    A, B = map(int, r_input().split())

    if A < N:
        stack.append(N - A)

print(sum(stack) - max(stack))

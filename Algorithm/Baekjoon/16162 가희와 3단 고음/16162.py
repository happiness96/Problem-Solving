import sys
r_input = sys.stdin.readline

# N: 참가자들의 음의 개수, A, D: 고음의 첫 항과 공차
N, A, D = map(int, r_input().split())

Note = list(map(int, r_input().split()))

X = 0

for i in range(N):
    if Note[i] == A:
        X += 1
        A += D

print(X)

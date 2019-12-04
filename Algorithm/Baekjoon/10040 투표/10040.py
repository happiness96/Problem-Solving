import sys
r_input = sys.stdin.readline

# N: 경기의 수, M: 위원의 수
N, M = map(int, r_input().split())

interesting = []

for _ in range(N):
    interesting.append(int(r_input()))

vote = [0] * N

for _ in range(M):
    B = int(r_input())

    for i in range(N):
        if interesting[i] <= B:
            vote[i] += 1
            break

print(vote.index(max(vote)) + 1)

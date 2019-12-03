import sys
r_input = sys.stdin.readline

# N: 학생들의 수, K: 한 방에 배정할 수 있는 최대 인원 수
N, K = map(int, r_input().split())
students = {grade: [0] * 2 for grade in range(1, 4)}

for _ in range(N):
    # S: 성별 (0: 여학생, 1: 남학생), Y: 학년
    S, Y = map(int, r_input().split())

    if Y < 3:
        S = 0

    students[(Y+1)//2][S] += 1

total = 0

for i in range(1, 4):
    for j in range(2):
        total += students[i][j] // K

        if students[i][j] % K:
            total += 1

print(total)

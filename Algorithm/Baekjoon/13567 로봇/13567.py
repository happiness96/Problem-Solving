import sys
r_input = sys.stdin.readline

# M: 정사각형 S의 한 변의 길이, n: 명령어의 개수
M, n = map(int, r_input().split())

row, col = 0, 0     # 현재 로봇의 위치
way = 1         # 방향 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽


def move_robot(dist):           # 로봇 이동시키기
    global row, col

    if way == 0:
        row += dist

    elif way == 1:
        col += dist

    elif way == 2:
        row -= dist

    else:
        col -= dist

    if not 0 <= row <= M or not 0 <= col <= M:      # 로봇이 정사각형 밖으로 나간다면
        print(-1)
        exit()


for _ in range(n):
    a, b = map(str, r_input().rstrip().split())
    b = int(b)

    if a == 'MOVE':
        move_robot(b)

    else:           # 방향 전환
        if not b:
            way -= 1

            if way < 0:
                way = 3

        else:
            way += 1

            if way == 4:
                way = 0

print(col, row)

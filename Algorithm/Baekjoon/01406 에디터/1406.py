# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

cursor_left = list(r_input().rstrip())          # 커서 왼쪽에 있는 문자
cursor_right = []                               # 커서 오른쪽에 있는 문자

N = int(r_input())              # 명령어의 개수

for _ in range(N):
    order = r_input().rstrip()

    if order == 'L':                # 커서를 왼쪽으로 한 칸 옮김
        if cursor_left:
            cursor_right.append(cursor_left.pop())

    elif order == 'D':              # 커서를 오른쪽으로 한 칸 옮김
        if cursor_right:
            cursor_left.append(cursor_right.pop())

    elif order == 'B':              # 커서의 왼쪽에 있는 문자를 지움
        if cursor_left:
            cursor_left.pop()

    else:                            # 커서의 왼쪽에 문자를 추가함
        cursor_left.append(order[2:])

print(''.join(cursor_left) + ''.join(cursor_right[::-1]))

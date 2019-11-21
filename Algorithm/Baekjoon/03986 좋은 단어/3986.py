# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 단어의 개수
cnt = 0

for _ in range(N):
    s = input().rstrip()
    stack = []

    for c in s:
        if stack and stack[-1] == c:            # 스택에 들어있는 마지막 문자와 일치하며 pop
            stack.pop()
        else:
            stack.append(c)

    if not stack:           # 스택이 비어있는지 검사
        cnt += 1

print(cnt)

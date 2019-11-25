# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 단어의 개수

words = []                  # 단어들
for i in range(N):
    words.append(r_input().rstrip())

words.sort()
cnt = N

for i in range(N):
    for j in range(i+1, N):
        if words[j].startswith(words[i]):
            cnt -= 1
            break

print(cnt)

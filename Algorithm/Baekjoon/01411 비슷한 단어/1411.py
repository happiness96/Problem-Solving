# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 단어의 개수
cnt = 0

words = []
cons = {}

for i in range(N):
    words.append(r_input().rstrip())

    cons[i] = [[] for _ in range(26)]

    for j in range(len(words[i])):
        cons[i][ord(words[i][j]) - 97].append(j)

cons_list = {}

for i in range(N):
    cons_list[i] = []

    for j in cons[i]:
        if j:
            cons_list[i].append(j)

    cons_list[i].sort()

for i in range(N - 1):
    for j in range(i + 1, N):
        if cons_list[i] == cons_list[j]:
            cnt += 1

print(cnt)

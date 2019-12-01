# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())              # 단어의 수

words = []

for _ in range(N):
    words.append(r_input().rstrip())

for w in words:
    if w[::-1] in words:
        print(len(w), w[len(w) // 2])
        break

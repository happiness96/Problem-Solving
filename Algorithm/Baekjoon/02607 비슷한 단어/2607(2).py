# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 단어의 개수
first_word = [0] * 26             # 첫 번째 단어 구성
cnt = 0

for c in r_input().rstrip():
    first_word[ord(c)-65] += 1

for i in range(N-1):
    second_word = [0] * 26            # 두 번째 단어 구성

    for c in r_input().rstrip():
        second_word[ord(c)-65] += 1

    gap = 0
    for i in range(26):
        if first_word[i] != second_word[i]:
            gap += abs(first_word[i] - second_word[i])

    if abs(sum(first_word) - sum(second_word)) < 2 and gap <= 2:
        cnt += 1

print(cnt)

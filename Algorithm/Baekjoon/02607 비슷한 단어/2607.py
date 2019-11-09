# -*- encoding: utf-8 -*-
import sys
from copy import deepcopy

r_input = sys.stdin.readline

n = int(r_input())  # 단어의 개수
first_word = list(r_input().rstrip())  # 첫 번째 단어
length = len(first_word)  # 첫 번째 단어의 길이
cnt = 0  # 첫 번째 단어와 비슷한 단어의 개수

for _ in range(n - 1):
    copy_word = deepcopy(first_word)
    input_word = list(r_input().rstrip())  # 비교할 단어
    temp = []
    input_length = len(input_word)

    if abs(input_length - length) > 1:  # 단어의 길이가 2개 이상 차이 날 경우
        continue

    if length > input_length:
        nope = 0
        for i in range(input_length):
            c = input_word.pop()

            if c in copy_word:
                copy_word.pop(copy_word.index(c))

            else:
                nope = 1
                break

        if nope:
            continue

        else:
            cnt += 1

    elif length < input_length:
        nope = 0
        for i in range(length):
            c = copy_word.pop()

            if c in input_word:
                input_word.pop(input_word.index(c))

            else:
                nope = 1
                break

        if nope:
            continue

        else:
            cnt += 1

    else:
        nope = 0
        for i in range(length):
            c = copy_word[i]
            if c in input_word:
                input_word.pop(input_word.index(c))

            else:
                nope += 1

        if nope < 2:
            cnt += 1

print(cnt)

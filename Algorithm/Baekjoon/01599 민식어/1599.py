# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())          # 민식어의 단어 개수

min_lan = {}        # {key: 영어, value: 민식어}
min_to_eng = {}         # 민식어를 영어로

tmp = list(map(str, 'a b k d e g h i l m n ng o p r s t u w y'.split()))

for i in range(20):
    min_to_eng[tmp[i]] = chr(97 + i)

for _ in range(N):
    eng = ''

    word = r_input().rstrip()
    length = len(word)

    ng = 0

    for i in range(length):
        if ng:
            ng = 0
            continue

        if i < length - 1 and word[i:i+2] == 'ng':
            ng = 1
            eng += min_to_eng['ng']

        else:
            eng += min_to_eng[word[i]]

    min_lan[eng] = word

for w in sorted(min_lan):
    print(min_lan[w])

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

key = r_input().rstrip()                # 키
cryptogram = r_input().rstrip()         # 암호문

save = [[] for _ in range(len(key))]        # 암호문 열별로 저장

length = len(cryptogram) // len(key)         # 한 열의 크기

for i in range(len(cryptogram)):
    save[i // length].append(cryptogram[i])

order = []
for i in range(26):
    ch = chr(65 + i)

    if ch in key:
        for j in range(len(key)):
            if key[j] == ch:
                order.append(j)

for a in range(length):
    for b in range(len(key)):
        print(save[order.index(b)][a], end='')

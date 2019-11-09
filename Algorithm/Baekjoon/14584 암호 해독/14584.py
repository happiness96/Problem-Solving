# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

password = r_input().rstrip()       # 암호문

N = int(r_input())            # 사전에 있는 단어의 수
dictionary = []         # 사전

for i in range(N):
    dictionary.append(r_input().rstrip())

for i in range(26):
    decoding = ''
    for c in password:               # 암호문 복호화
        ind = ord(c) + i

        if ind > 122:
            ind -= 26

        decoding += chr(ind)

    for word in dictionary:
        if word in decoding:
            print(decoding)
            exit()

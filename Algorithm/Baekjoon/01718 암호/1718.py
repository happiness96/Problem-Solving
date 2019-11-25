# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

string = r_input().rstrip()         # 평문
key = r_input().rstrip()            # 암호화 키

length = len(key)                   # 암호화 키의 길이

for i in range(len(string)):
    if string[i] == ' ':
        print(' ', end='')

    else:
        ch = ord(string[i]) - (ord(key[i % length]) - 96)

        if ch < 97:
            ch += 26

        print(chr(ch), end='')

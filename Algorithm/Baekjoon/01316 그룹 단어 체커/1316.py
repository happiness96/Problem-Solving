# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N: 단어의 개수
N = int(r_input())
cnt = 0

for _ in range(N):
    chk = [0] * 26
    word = r_input().rstrip()
    length = len(word)

    chk[ord(word[0]) - 97] = 1
    flag = 1

    for i in range(1, length):
        if word[i] != word[i - 1]:
            if chk[ord(word[i]) - 97]:
                flag = 0
                break
            else:
                chk[ord(word[i]) - 97] = 1

    cnt += flag

print(cnt)

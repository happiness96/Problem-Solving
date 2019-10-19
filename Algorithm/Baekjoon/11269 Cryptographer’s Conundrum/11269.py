#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

text = r().rstrip()     # 입력받은 문자열
name = 'PER'
cnt = 0                 # 바꿔야할 문자의 수

for i in range(len(text)):
    if text[i] != name[i%3]:
        cnt += 1

print(cnt)

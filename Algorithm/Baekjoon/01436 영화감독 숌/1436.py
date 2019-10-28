#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # N번째 영화

num = 666
cnt = 0

while 1:
    if '666' in str(num):
        cnt += 1
        if cnt == N:
            print(num)
            break
    num += 1

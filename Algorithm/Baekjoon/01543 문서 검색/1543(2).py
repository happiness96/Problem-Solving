# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

doc = r_input().rstrip()            # 문서의 길이
find_me = r_input().rstrip()        # 검색하고 싶은 단어
cnt = 0         # 등장하는 횟수
ind = 0         # 현재 인덱스
length = len(find_me)

while ind <= len(doc) - length:
    if doc[ind:ind + length] == find_me:
        cnt += 1
        ind += length
        continue

    ind += 1

print(cnt)

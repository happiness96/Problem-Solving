# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

doc = r_input().rstrip()            # 문서
find_me = r_input().rstrip()        # 검색하고 싶은 단어

print(doc.count(find_me))

#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

K, L = map(int, r().split())        # K: 수강 가능 인원, L: 대기 목록의 길이

sugang1 = {}                # key: 수강 신청 순서, value: 학번
sugang2 = {}                # key: 학번, value: 수강 신청 순서

for i in range(1, L+1):
    student_id = r().rstrip()
    sugang1[i] = student_id
    sugang2[student_id] = i
    
cnt = 0
index = 0

for i in sugang1.keys():
    if sugang2[sugang1[i]] == i:
        cnt += 1
        print(sugang1[i])
        
    if cnt == K: break

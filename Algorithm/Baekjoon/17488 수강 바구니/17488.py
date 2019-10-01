#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline
n,m = map(int,r().split())      # n : 학생 수, m : 과목 수

l = {}      # l : 수강 제한 인원
i = 1
for c in map(int,r().split()):
    l[i] = c
    i+=1

result = {}     # 수강신청 결과

sugang1 = {}     # 1차 수강바구니
for i in range(1,n+1):          # 각 사람이
    for j in map(int,r()[:-3].split()):         # 수강신청한 과목
        if j in sugang1: sugang1[j].append(i)
        else: sugang1[j] = [i]

# 1차 수강바구니  인원 초과 체크
for i in sugang1:       # 각 과목에 대해
    if len(sugang1[i]) <= l[i]:     # 수강 신청 과목이 초과하지않았다면
        for j in sugang1[i]:        # 수강 신청에 성공한 과목을 result에 삽입
            if j in result: result[j].append(i)
            else: result[j]=[i]
    l[i] -= len(sugang1[i])     # 수강 신청한 인원만큼 감소

sugang2 = {}    # 2차 수강바구니
for i in range(1,n+1):      #각 사람이
    for j in map(int,r()[:-3].split()):        #수강신청한 과목
        if j in sugang2: sugang2[j].append(i)
        else: sugang2[j] = [i]

for i in sugang2:       # 각 과목에 대해
    if len(sugang2[i]) <= l[i]:     # 수강 신청 과목이 초과하지않았다면
        for j in sugang2[i]:        # 수강 신청에 성공한 과목을 result에 삽입
            if j in result: result[j].append(i)
            else: result[j]=[i]

for i in range(1,n+1):      #결과 출력
    if not i in result:
        print("망했어요")
    else:
        for j in sorted(result[i]):
            print(j,end=' ')
        print()

#-*- encoding: utf-8 -*-
import sys;
r=sys.stdin.readline
member={}           #회원들의 정보를 담을 dictionary 생성
for i in range(int(r())):
    age,name = map(str,r().rstrip().split())
    age = int(age)
    if age in member:
        member[age].append(name)    #나이를 key 값으로, 이름을 value값으로 넣는다.
    else: member[age]=[name]
    
for i in sorted(member):    #key값(나이) 기준으로 정렬
    for j in member[i]:
        print(i,j)

#-*- encoding: utf-8 -*-
import sys;r=sys.stdin.readline
from itertools import combinations
n,m,d=map(int,r().split())  # n : 행, m : 열, d : 공격 거리 제한      *궁수는 m+1행에 배치
monster = {}    #몬스터 배치
result=[]   #결과값
items=[t for t in range(m)]     #0부터 m-1까지


for i in range(n):monster[i]=list(map(int,r().split()))
items_2=list(combinations(items,3))     #궁수 3명 뽑아내는 조합

def round_start(archer_row, archer_col):
    is_killed=0
    for i in range(d):          # 제한 거리만큼 반복
        check=killed_row=killed_col=0
        for j in range(-i, i+1):    #왼쪽부터 차례로 탐색
            mon_row,mon_col=archer_row-i-1+abs(j),archer_col+j
            if mon_row<0 or mon_col<0 or mon_col>m-1:continue
            if monster[mon_row][mon_col]==1:check,killed_row,killed_col=1,mon_row,mon_col;break
        if check:is_killed=(killed_row,killed_col);break
    return is_killed;

def get_result(archers):
    kill=0
    back_up_monsters={}
    for i in range(n):  #궁수의 r 위치
        killed_monsters={}
        for archer in archers:
            temp=round_start(n-i,archer)    #각 위치의 궁수들이 kill한 몬스터의 r,c 반환
            if temp: killed_monsters[temp]=0;back_up_monsters[temp]=0
        kill+=len(killed_monsters)
        for c in killed_monsters:monster[c[0]][c[1]]=0
    for c in back_up_monsters:monster[c[0]][c[1]]=1
    return kill;

for test in items_2:        #궁수의 위치에 따라 반복
    result.append(get_result(test))
print(max(result))

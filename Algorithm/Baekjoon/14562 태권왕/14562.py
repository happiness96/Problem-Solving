#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

C = int(r())            # 테스트 케이스의 개수

def kick(n):       # n: 최소 발차기 횟수
    global score
    
    temp = {}
    
    for s in score:
        a, b = s[0]+1, s[1]         # 일반 연속 발차기
        if a == b:
            print(n)
            return
        else:
            temp[a, b] = 0
        
        a, b = s[0] * 2, s[1] + 3       # 엄청난 연속 발차기
        if a == b:
            print(n)
            return
        elif a < b:         # 내 점수가 상대의 점수보다 커버리면 의미가 없음
            temp[a, b] = 0
    
    score = temp
    kick(n+1)

for i in range(C):
    S, T = map(int, r().split())        # S: 현재 태균이의 점수, T: 상대의 점수
    score = {}              # 두 사람의 점수
    
    if S == T:
        print(0)
    else:
        score[S, T] = 0
        kick(1)

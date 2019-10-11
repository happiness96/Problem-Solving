#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

score_sum = [0]*3           # 세 후보들의 점수
three_score = [0]*3     # 세 후보들이 3점을 받은 횟수
two_score = [0]*3       # 세 후보들이 2점을받은 횟수

N = int(r())                # 반 학생들의 수

for i in range(N):
    score = list(map(int,r().split()))
    
    for j in range(3):
        score_sum[j] += score[j]        # 세 후보들의 점수를 더한다
        
        if score[j] == 3:               # 점수가 3점인 경우
            three_score[j] += 1
            
        if score[j] == 2:               # 점수가 2점인 경우
            two_score[j] += 1


max_score = max(score_sum)          # 최대 점수

if score_sum.count(max_score) == 1:     #최대 점수가 한 사람인 경우
    print(score_sum.index(max_score) + 1, max_score)
    
else:               # 최대 점수가 여러명일 경우
    same_score = []
    for i in range(3):
        if score_sum[i] == max_score:
            same_score.append(i)
            
    temp = []
    for i in same_score:
        temp.append(three_score[i])
    
    max_three_score = max(temp)     # 3점의 개수 최대값
    
    if temp.count(max_three_score) == 1:
        print(same_score[temp.index(max_three_score)] + 1, max_score)
    
    else:                # 만약 3점을 받은 횟수도 같다면
        same_three_score = []
        for i in same_score:
            if three_score[i] == max_three_score:
                same_three_score.append(i)
                
        temp = []
        for i in same_three_score:
            temp.append(two_score[i])
        
        max_two_score = max(temp)
        
        if temp.count(max_two_score) == 1:
            print(same_three_score[temp.index(max_two_score)] + 1, max_score)
        
        else:
            print(0, max_score)

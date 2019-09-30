#-*- encoding: utf-8 -*-
n = int(input())            #문제의 수
correct_answer = input()        #정답
score = [0]*3      #각 사람이 맞춘 문제의 수
guess = ['ABC','BABC','CCAABB']     #각 사람이 찍는 순서
name = ['Adrian','Bruno','Goran']   #각 사람의 이름

for i in range(n):      #각 문제에대해
    for j in range(3):      #3사람의 답안을 비교
        if correct_answer[i]==guess[j][i%len(guess[j])]:
            score[j]+=1

max_score=max(score)        #최대 점수
print(max_score)

for i in range(3):          #최대 점수를 받은 사람들을 순서대로 출력
    if score[i]==max_score:
        print(name[i])

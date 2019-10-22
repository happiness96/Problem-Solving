#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())            # 학생의 수
total = 0                  # 학생들의 점수

for i in range(N):
    score = r().rstrip()
    score = score.replace('0', '9')
    score = score.replace('6', '9')
    
    total += min(int(score), 100)

avr = total / N         # 평균 점수

def round(num):
    if num%1 >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    
print(round(avr))

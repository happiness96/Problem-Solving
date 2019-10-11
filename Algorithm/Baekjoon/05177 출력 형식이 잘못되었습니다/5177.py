#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

K = int(r())            # 테스트 케이스 수

def find_valid_string(s):
    blank = 0       # 공백 유무
    sign = 0        # 특수 부호의 뒤인지 판별
    
    valid_string = ''
    
    for word in s:
        if word == ' ':             # 공백인 경우
            blank = 1
        
        elif word in '([{':           # 특수문자들 처리
            valid_string += '('
            sign = 1
        
        elif word in ')]}':
            valid_string += ')'
            sign = 1
        
        elif word in ',;':
            valid_string += ','
            sign = 1
            
        elif word in '.:':
            valid_string += word
            sign = 1
            
        else:               # 일반 문자가 올 경우
            if sign:        # 특수 부호의 뒤일 경우
                sign = 0
                valid_string += word
                
            elif blank:     # 앞에 공백이 있었을 경우
                blank = 0
                valid_string += ' ' + word
            
            else:           # 일반 문자가 연속해서 올 경우
                valid_string += word
                
    if valid_string[0] == ' ':      # 문자열의 맨 앞 공백 무시
        valid_string = valid_string[1:]
            
    return valid_string

for i in range(K): 
    s1 = r().rstrip().lower()
    s2 = r().rstrip().lower()
    
    valid_s1 = find_valid_string(s1)
    valid_s2 = find_valid_string(s2)
    
    print('Data Set ' + str(i+1), end=': ')
    print('equal'if valid_s1 == valid_s2 else 'not equal')
    print()

#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

S = r().rstrip()        # 문자열 입력

temp = ''               # 임시로 저장할 문자열
tag = 0                 # 1: 태그인 경우, 0: 태그가 아닌 경우

for i in range(len(S)):
    word = S[i]         # 현재 문자
    
    if word == '<':     # 태그 시작
        print(temp[::-1], end='')       # 저장되어 있는 단어들을 뒤집어 출력
        temp = '<'
        tag = 1
        continue
    
    if tag == 1:        # 태그인 경우
        temp += word
        
        if word == '>':     # 태그가 닫히면 출력해주고 임시 문자열을 비운다.
            print(temp, end='')
            temp = ''
            tag = 0
        continue
    
    if word == ' ':         # 공백을 만나면 단어를 뒤집어 출력
        print(temp[::-1], end=' ')
        temp = ''
        continue
    
    temp += word
    
    if i == len(S)-1:       # 문자열의 맨 마지막인 경우
        print(temp[::-1])

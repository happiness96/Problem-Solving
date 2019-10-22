#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # 테스트 케이스의 개수

for i in range(T):
    k = int(r())            # 단어의 수
    words = {}
    
    for j in range(k):
        words[j] = r().rstrip()
    
    non = 1
    
    for j in range(k):
        for h in range(k):
            
            if j!=h:
                is_palindrome = words[j] + words[h]
                
                if is_palindrome == is_palindrome[::-1]:        # 팰린드롬인지 체크
                    non = 0
                    print(is_palindrome)
                    
                    break
        if non == 0:
            break
        
    if non:         # 팰린드롬이 없다면
        print(0)

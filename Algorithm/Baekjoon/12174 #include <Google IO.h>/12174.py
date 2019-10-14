#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # T: 테스트 케이스의 개수

for i in range(T):
    B = int(r())        # B: 문자열의 크기
    
    byte_string = r().rstrip()  # 바이트 문자열
    
    print('Case #' + str(i + 1), end =': ')
    for j in range(B):
        eight_bit = byte_string[8*j:8*(j+1)]
        eight_bit = eight_bit.replace('O','0')
        eight_bit = eight_bit.replace('I','1')
        print(chr(int(eight_bit,2)),end='')
    print()

#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # 테스트 케이스의 수

for i in range(T):
    num = r().rstrip()
    cnt = 0
    
    while True:
        if num == '6174':
            print(cnt)
            break
        
        if len(num) != 4:           # 앞자리 0 채워주기
            num = '0' * (4-len(num)) + num
        
        cnt += 1
        pack = {}
        
        for n in num:
            i_n = int(n)
            if i_n in pack:
                pack[i_n] += 1
            else:
                pack[i_n] = 1
        
        kar = ''
        for p in sorted(pack):
            kar += str(p) * pack[p]
        
        num = str(int(kar[::-1]) - int(kar))

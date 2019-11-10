# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

die_list = []           # 주사위
dup = 0                 # 중복 수

for num in map(int, r_input().split()):
    if num in die_list:
        dup = num
    
    else:
        die_list.append(num)

if len(die_list) == 3:          # 세개의 눈이 모두 다른 경우
    print(max(die_list) * 100)

elif len(die_list) == 2:        # 두개의 눈이 같은 경우
    print(1000 + dup * 100)

else:                           # 세 개의 눈이 모두 같은 경우
    print(10000 + dup * 1000)

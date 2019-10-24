#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())            # 테스트 케이스의 수


def find_point(num):
    start = 1
    temp = 1        # 누적 합 (x = 1)
    
    while 1:
        temp += start
        if temp <= num <= temp + start:
            start +=1
            x = num - temp + 1
            y = start - (num - temp)
            return x, y
        start += 1


for i in range(T):
    num1, num2 = map(int, r().split())      # 점 1의 값, 점 2의 값
    
    # 점 1의 좌표 찾기
    x1 = y1 = 0
    
    if num1 == 1:
        x1 = y1 = 1
    else:
        x1, y1 = find_point(num1)
    
    # 점 2의 좌표 찾기
    x2 = y2 = 0
    
    if num2 == 1:
        x2 = y2 = 1
    
    else:
        x2, y2 = find_point(num2)
    
    
    # Find value
    x3, y3 = x1 + x2, y1 + y2
    start = 1
    result = 1
    
    for i in range(1, y3):
        result += i
    
    gap = y3 + 1
    for i in range(x3-1):
        result += gap
        gap += 1
    print(result)

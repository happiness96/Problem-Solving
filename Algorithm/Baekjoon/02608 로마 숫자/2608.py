#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

sign = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
half = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

first = r().rstrip()            # 첫번째 로마 숫자
second = r().rstrip()           # 두번째 로마 숫자

total = 0       # 합계

def roman_to_number(roman):          # 로마자를 숫자로
    result = 0          # 반환할 숫자
    count = 1           # 연속으로 나오는 로마자 개수
    check = 0           # half에 있는 로마자가 나올 경우
    
    if len(roman) == 1:
        return sign[roman]
    
    for i in range(1,len(roman)):
        temp = roman[i-1] + roman[i]        # half에 있는 로마자 체크
        
        if check :
            check = 0
            if i == len(roman)-1:
                result += sign[roman[i]]
            continue
        
        if roman[i] == roman[i-1]:    #연속으로 나오는 경우
            count += 1
            
        elif temp in half:              # half에 있는 로마자일 경우
            result += half[temp]
            count = 1
            check = 1
                
        elif sign[roman[i]] < sign[roman[i-1]]:
            result += count * sign[roman[i-1]]
            count = 1
        
        if check == 0 and i == len(roman)-1:               # 마지막 문자일 경우
            if sign[roman[i]] < sign[roman[i-1]]:
                result += sign[roman[i]]
            else:
                result += count * sign[roman[i-1]]
        
    return result

def number_to_roman(number):        # 숫자를 로마자로
    result= ''
    
    thousand = number // 1000       # 천의 자리
    result += thousand * 'M'
    number -= thousand * 1000
    
    hundred = number // 100         # 백의자리
    if hundred >= 5:
        if hundred == 9:
            result += 'CM'
        else:
            result += 'D' + 'C' * (hundred - 5)
    else:
        if hundred == 4:
            result += 'CD'
        else:
            result += 'C' * hundred
    number -= hundred * 100
    
    deca = number // 10             # 십의 자리
    if deca >= 5:
        if deca == 9:
            result += 'XC'
        else:
            result += 'L' + 'X' * (deca - 5)
    else:
        if deca == 4:
            result += 'XL'
        else:
            result += 'X' * deca
    number -= deca * 10
    
    if number >= 5:                 # 일의 자리
        if number == 9:
            result += 'IX'
        else:
            result += 'V' + 'I' * (number - 5)
    else:
        if number == 4:
            result += 'IV'
        else:
            result += 'I' * number
            
    return result

total = roman_to_number(first) + roman_to_number(second)

print(total)
print(number_to_roman(total))

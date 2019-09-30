#-*- encoding: utf-8 -*-
left = 'qwertyasdfgzxcvb'     #왼손으로 누르는 문자    
right = 'uiophjklnm'          #오른손으로 누르는 문자
c_left = c_right = blank = 0        #왼손과 오른손으로 누르는 키 개수, blank는 공백과 shift 개수

s = input()
for c in s:             #각 문자에 따라 오른손, 왼손, blank(+shift) 누르는 횟수 계산
    num = ord(c)
    if chr(num) in left: c_left+=1
    elif chr(num) in right: c_right+=1
    elif c==' ': blank+=1
    else: 
        if chr(num+32) in left: c_left+=1
        elif chr(num+32)in right: c_right+=1
        blank+=1

if c_left >= c_right + blank: c_right += blank          #blank의 개수에 따라 왼쪽, 오른쪽 누른 횟수 차가 최소가 되도록 
elif c_right >= c_left + blank: c_left += blank
else:
    if c_right>c_left:
        blank-=c_right - c_left
        c_right+=blank//2
        c_left = c_right
    elif c_left>c_right:
        blank-=c_left - c_right
        c_left+=blank//2
        c_right = c_left
    if blank % 2: c_left+=1
print(c_left, c_right)

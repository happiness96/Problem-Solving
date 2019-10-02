#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

s = r()[:-1]        #변수 선언문

init_variable = ''
for i in range(len(s)):         # 기본 변수형
    if s[i]==' ': break
    init_variable += s[i]

variables = list(map(str,s[i+1:].split()))

for v in variables: 
    variable = ''   # 변수명
    sign = ''       # 기호
    for i in range(len(v)-1):
        if v[i] in '*&': sign += v[i]
        elif v[i] == '[': sign += ']'
        elif v[i] == ']': sign += '['
        else: variable += v[i]
    print(init_variable + sign[::-1], variable + ';')

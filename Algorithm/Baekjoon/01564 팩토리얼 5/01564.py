# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N = int(r_input())      # 정수 N
result = 1              # 결과

for i in range(1, N+1):
    temp = str(result * i)

    while True:
        if temp[-1] == '0':
            temp = temp[:-1]
        else:
            break
    length = len(temp)
    if length > 15:
        temp = temp[length-15:]

    result = int(temp)

print(temp[len(temp)-5:])

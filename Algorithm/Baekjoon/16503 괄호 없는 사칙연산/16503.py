#-*- encoding: utf-8 -*-
K1,O1,K2,O2,K3=map(str,input().split())     # 식의 형태
result1 = result2 = 0                       # 결과값

K1 = int(K1)
K2 = int(K2)
K3 = int(K3)

def calculate(first, op, second):       # 계산  함수
    result = 0
    if op=='+': result = first + second
    elif op=='-': result = first - second
    elif op=='*': result = first * second
    elif op=='/':               # 피연산자중 하나가 음수일 때 조건 처리
        minus = 0
        if first < 0:
            minus+=1
            first = -first
        if second < 0:
            minus+=1
            second = -second
        result = first // second
        if minus == 1: result = -result 
    return result

result1 = calculate(K1,O1,K2)
result1 = calculate(result1,O2,K3)

result2 = calculate(K2,O2,K3)
result2 = calculate(K1,O1,result2)

print(min(result1, result2))
print(max(result1, result2))

#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # 수식의 길이

number = []         # 숫자
op = []             # 연산자
result = []         # 연산 결과

expression = r().rstrip()       # 수식

for i in range(N):
    if i%2:         # 수식에서 홀수 인덱스에 있는 것들은 operation에 삽입
        op.append(expression[i])
    else:           # 짝수 인덱스에 있는 것들은  number에 삽입
        number.append(int(expression[i]))


def calculator(num1, oper, num2):        # 연산 함수
    calc_result = 0
    
    if oper == '+':
        calc_result = num1 + num2
        
    elif oper == '-':
        calc_result = num1 - num2
        
    elif oper == '*':
        calc_result = num1 * num2
        
    return calc_result


def calculate(first_calculate):         # first_calculate를 우선 수행하고 나온 결과를 result에 추가하는 함수
    calc_result = number[0]
    check = 0           # 1: 다음 연산자를 수행했을 경우 (다음에 괄호가 나오는 경우)
    
    for i in range(N//2):
        if check :      # 다음 연산을 이미 수행해주었다면 
            check = 0
            continue
        
        if i + 1 in first_calculate:        # 다음 연산자를 우선 수행해야 한다면
            calc_result = calculator(calc_result, op[i], calculator(number[i+1], op[i+1], number[i+2]))
            check = 1
            
        else:
            calc_result = calculator(calc_result, op[i], number[i+1])
            
    result.append(calc_result)


def find_first_calculate(first_calc_list):          # DFS방식, 먼저 계산할 괄호 연산자 탐색
    calculate(first_calc_list)
    
    if not first_calc_list[-1] in [N//2-1, N//2-2]:     # 마지막 괄호가 아니라면 더 깊이 탐색
        for i in range(first_calc_list[-1] + 2, N//2):
            find_first_calculate(first_calc_list + [i])


calculate([])           # 먼저 괄호가 없을 경우를 계산

for i in range(1,N//2):
    find_first_calculate([i])
    
print(max(result))

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


def calculate(calc_node, number_list, op_list):          # DFS방식, 계산을 진행할 op인덱스 탐색
    temp_number_list = [] + number_list
    temp_op_list = [] + op_list
    
    temp_number_list.insert(calc_node, calculator(temp_number_list.pop(calc_node), temp_op_list.pop(calc_node), temp_number_list.pop(calc_node)))
    
    if len(temp_number_list) == 1:
        result.append(temp_number_list[0])
    else:
        for i in range(len(temp_op_list)):
            calculate(i, temp_number_list, temp_op_list)


if N == 1:
    result = number

for i in range(N//2):
    calculate(i, number, op)
    
print(max(result))

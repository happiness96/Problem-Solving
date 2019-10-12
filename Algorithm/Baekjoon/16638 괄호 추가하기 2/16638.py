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


def get_number_list(f_list, numbers, ops):         # 연산 우선 수행을 마치고 남은 숫자들 반환
    result_list = []
    
    check = 0               # 1: 다음 연산자가 먼저 수행해야할 리스트에 포함될 경우
    
    if len(numbers) == 1:       # 숫자가 하나만 들어올 경우
        result_list = numbers
        
    for i in range(len(ops)):
        if check:           # 연산자를 이미 수행했을 경우
            if i in f_list:     # * 가 연속해서 나올 경우
                result_list.append(calculator(result_list.pop(), ops[i], numbers[i+1]))
            else:
                check = 0
                
            if check == 0 and i == len(ops)-1:         # 마지막 숫자 넣기
                result_list.append(numbers[i+1])
                
            continue
        
        if i in f_list:
            result_list.append(calculator(numbers[i], ops[i], numbers[i+1]))
            check = 1
        
        else:
            result_list.append(numbers[i])
            if i == len(ops)-1:         # 마지막 숫자 넣기
                result_list.append(numbers[i+1])
            
    return result_list


def calculate(first_calculate):         # 괄호(first_calculate)를 우선 수행하고, *(second_calculate)를 우선 수행해서 나온 결과를 result에 추가
    
    first_numbers = get_number_list(first_calculate, number, op)      # 괄호 연산 마치고 남은 숫자들을 리스트로 가져온다
    first_op = []
    
    for i in range(N//2):               # 괄호를 수행하고 남은 op만 first_op에 담는다
        if not i in first_calculate:
            first_op.append(op[i])
    
    second_calculate = []               # 곱셈이 나오는 op 인덱스(두번째로 우선 수행해야 할 것)
    
    for i in range(len(first_op)):
        if first_op[i] == '*':
            second_calculate.append(i)
    
    second_numbers = get_number_list(second_calculate, first_numbers, first_op)       # 곱셈 연산을 마치고 남은 숫자들을 리스트로 가져온다.
    second_op = []
    
    for i in range(len(first_op)):              # 곱셈 연산을 수행하고 남은 op만 second_op에 담는다
        if not i in second_calculate:
            second_op.append(first_op[i])
    
    calc_result = second_numbers[0]

    for i in range(len(second_op)):
        calc_result = calculator(calc_result, second_op[i], second_numbers[i+1])

    result.append(calc_result)


def find_first_calculate(first_calc_list):          # DFS방식, 먼저 계산할 괄호 연산자 탐색
    calculate(first_calc_list)
    
    if not first_calc_list[-1] in [N//2-1, N//2-2]:     # 마지막 괄호가 아니라면 더 깊이 탐색
        for i in range(first_calc_list[-1] + 2, N//2):
            find_first_calculate(first_calc_list + [i])


calculate([])           # 먼저 괄호가 없을 경우를 계산

for i in range(N//2):
    find_first_calculate([i])
    
print(max(result))

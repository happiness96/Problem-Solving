# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

T = int(r_input())      # 테스트 케이스의 수


def find_result(length, num, result, current, op, temp):            # 경우의 수 찾기
    if length == num:
        if temp:
            if result:
                result += op + ' '.join(temp)
            else:
                result += ' '.join(temp)

            temp_num = int(''.join(temp))
            if op == '+':
                current += temp_num
            else:
                current -= temp_num
        else:
            if result:
                result += op + str(num)
            else:
                result += str(num)

            if op == '+':
                current += num
            else:
                current -= num
        if current == 0:
            if not result in final:
                final.append(result)
        return

    if temp:
        find_result(length, num+1, result, current, op, temp + [str(num + 1)])

        if result:
            result += op + ' '.join(temp)
        else:
            result += ' '.join(temp)

        temp_num = int(''.join(temp))

        if len(temp) > 1:
            if op == '+':
                current += temp_num
            else:
                current -= temp_num

            find_result(length, num + 1, result, current, '+', [str(num + 1)])
            find_result(length, num + 1, result, current, '-', [str(num + 1)])
            find_result(length, num + 1, result, current, '+', [])
            find_result(length, num + 1, result, current, '-', [])

    else:
        if result:
            result += op + str(num)
        else:
            result += str(num)

        if op == '+':
            current += num
        else:
            current -= num

        find_result(length, num + 1, result, current, '+', [str(num + 1)])
        find_result(length, num + 1, result, current, '-', [str(num + 1)])
        find_result(length, num + 1, result, current, '+', [])
        find_result(length, num + 1, result, current, '-', [])


for i in range(T):
    N = int(r_input())      # 자연수 N
    
    final = []
    find_result(N, 1, '', 0, '+', ['1'])
    find_result(N, 1, '', 0, '+', [])

    for t in sorted(final):
        print(t)
    print()

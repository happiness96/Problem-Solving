# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    n = int(r_input())

    result_list = []

    for _ in range(n):
        result_list.append(int(r_input()))

    result_list = result_list[::-1]

    stack = []
    result = []

    for i in range(1, n + 1):
        stack.append(i)
        result.append('+')

        while stack and result_list:
            if stack[-1] == result_list[-1]:
                result.append('-')

                stack.pop()
                result_list.pop()

            else:
                break

    print('\n'.join(result) if not result_list else 'NO')


if __name__ == '__main__':
    run()

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def chk_consist(string, comp):
    consist_string = [0] * 10

    if string[0] == '0':
        return 0

    for c in string:
        consist_string[int(c)] = 1

    if consist_string == comp:
        return 1
    else:
        return 0


for _ in range(3):
    x, y = map(str, r_input().rstrip().split())

    x = list(x)
    y = list(y)

    consist_x = [0] * 10
    consist_y = [0] * 10

    for a in x:
        consist_x[int(a)] = 1

    for b in y:
        consist_y[int(b)] = 1

    if consist_x == consist_y:          # 두 정수가 같은 구성으로 이루어진 경우
        print('friends')
        continue

    len_x = len(x)
    len_y = len(y)

    flag = 0

    if len_x != 1:
        for i in range(len_x):
            if i == 0:
                if x[i] != '0' and x[i + 1] != '9':
                    x[i] = str(int(x[i]) - 1)
                    x[i + 1] = str(int(x[i + 1]) + 1)

                    flag = max(flag, chk_consist(''.join(x), consist_y))

                    x[i] = str(int(x[i]) + 1)
                    x[i + 1] = str(int(x[i + 1]) - 1)

                if x[i] != '9' and x[i + 1] != '0':
                    x[i] = str(int(x[i]) + 1)
                    x[i + 1] = str(int(x[i + 1]) - 1)

                    flag = max(flag, chk_consist(''.join(x), consist_y))

                    x[i] = str(int(x[i]) - 1)
                    x[i + 1] = str(int(x[i + 1]) + 1)

            if i > 0:
                if x[i - 1] != '0' and x[i] != '9':
                    x[i - 1] = str(int(x[i - 1]) - 1)
                    x[i] = str(int(x[i]) + 1)

                    flag = max(flag, chk_consist(''.join(x), consist_y))

                    x[i - 1] = str(int(x[i - 1]) + 1)
                    x[i] = str(int(x[i]) - 1)

                if x[i - 1] != '9' and x[i] != '0':
                    x[i - 1] = str(int(x[i - 1]) + 1)
                    x[i] = str(int(x[i]) - 1)

                    flag = max(flag, chk_consist(''.join(x), consist_y))

                    x[i - 1] = str(int(x[i - 1]) - 1)
                    x[i] = str(int(x[i]) + 1)

            if flag:
                break

    if flag:
        print('almost friends')
        continue

    if len_y != 1:
        for i in range(len_y):
            if i == 0:
                if y[i] != '0' and y[i + 1] != '9':
                    y[i] = str(int(y[i]) - 1)
                    y[i + 1] = str(int(y[i + 1]) + 1)

                    flag = max(flag, chk_consist(''.join(y), consist_x))

                    y[i] = str(int(y[i]) + 1)
                    y[i + 1] = str(int(y[i + 1]) - 1)

                if y[i] != '9' and y[i + 1] != '0':
                    y[i] = str(int(y[i]) + 1)
                    y[i + 1] = str(int(y[i + 1]) - 1)

                    flag = max(flag, chk_consist(''.join(y), consist_x))

                    y[i] = str(int(y[i]) - 1)
                    y[i + 1] = str(int(y[i + 1]) + 1)

            if i > 0:
                if y[i - 1] != '0' and y[i] != '9':
                    y[i - 1] = str(int(y[i - 1]) - 1)
                    y[i] = str(int(y[i]) + 1)

                    flag = max(flag, chk_consist(''.join(y), consist_x))

                    y[i - 1] = str(int(y[i - 1]) + 1)
                    y[i] = str(int(y[i]) - 1)

                if y[i - 1] != '9' and y[i] != '0':
                    y[i - 1] = str(int(y[i - 1]) + 1)
                    y[i] = str(int(y[i]) - 1)

                    flag = max(flag, chk_consist(''.join(y), consist_x))

                    y[i - 1] = str(int(y[i - 1]) - 1)
                    y[i] = str(int(y[i]) + 1)

            if flag:
                break

    if flag:
        print('almost friends')
        continue

    print('nothing')

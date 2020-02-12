# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    s1 = r_input().rstrip()
    s2 = r_input().rstrip()

    length1 = len(s1)
    length2 = len(s2)

    stack = []
    ind = 0

    i = 0
    flag = 1
    while i < length1:
        if flag:
            stack.append(s1[i])
        else:
            flag = 1

        if s1[i] == s2[ind]:
            ind += 1

            if ind == length2:
                for _ in range(length2):
                    stack.pop()

                length = len(stack)
                j, k = max(0, length - length2), 0

                while j < length:
                    if stack[j] == s2[k]:
                        k += 1
                        j += 1

                    else:
                        if k == 0:
                            j += 1
                        else:
                            k = 0

                ind = k
            i += 1
        else:
            if ind == 0:
                i += 1

            else:
                flag = 0
                ind = 0

    print(''.join(stack) if stack else 'FRULA')


if __name__ == '__main__':
    run()

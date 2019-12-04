# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

T = r_input().rstrip()          # 전체 문자열
P = r_input().rstrip()          # 찾고자하는 문자열

cnt = 0         # 찾고자하는 문자열이 나온 횟수
result = []     # 찾고자하는 문자열이 나타나는 위치

length_T = len(T)
length_P = len(P)

pi = [0] * length_P


def make_pi_list():
    i = 0
    j = 1

    while j < length_P:
        if P[i] == P[j]:
            pi[j] = i + 1
            i += 1
            j += 1

        elif i == 0:
            pi[j] = 0
            j += 1

        else:
            i = pi[i - 1]


def find_index():
    global cnt
    global result

    i = 0
    j = 0

    while j < length_T:
        if P[i] == T[j]:
            i += 1
            j += 1

            if i == length_P:
                cnt += 1
                result.append(str(j - length_P + 1))
                i = pi[i - 1]

        else:
            if i == 0:
                j += 1
            else:
                i = pi[i - 1]


make_pi_list()

find_index()

print(cnt)
print(' '.join(result))

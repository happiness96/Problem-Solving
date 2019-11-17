# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline
sys.setrecursionlimit(10**6)

S = r_input().rstrip()          # 만들고자하는 문자열
length = len(S)
N = int(r_input())              # A에 포함된 문자열의 개수

A = []

for i in range(N):
    A.append(r_input().rstrip())


def find_str():
    global S

    if S == '':
        print(1)
        exit()

    for a in A:
        if S.startswith(a):
            S = S[len(a):]
            find_str()
            S = a + S


find_str()

print(0)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# n: 수열의 길이, q: 쿼리의 개수
n, q = map(int, r_input().split())
save = list(map(int, r_input().split()))

for _ in range(q):
    querry = list(map(int, r_input().split()))

    if querry[0] == 1:
        a = querry[1] - 1
        b = querry[2] - 1
        print(sum(save[a: b + 1]))
        save[a], save[b] = save[b], save[a]

    else:
        print(sum(save[querry[1] - 1: querry[2]]) - sum(save[querry[3] - 1: querry[4]]))

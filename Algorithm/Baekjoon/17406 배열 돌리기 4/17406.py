# -*- encoding: utf-8 -*-
import sys
from itertools import permutations
r_input = sys.stdin.readline

N, M, K = map(int, r_input().split())         # N x M 행렬, 연산 K번 수행

array = {}              # 배열

for i in range(1, N+1):
    array[i] = [0] + list(map(int, r_input().split()))


def turn(left_r, left_c, right_r, right_c):         # 배열 돌리기
    for gap in range((right_r - left_r) // 2):

        temp1 = new_array[left_r][left_c]

        for i in range(left_c, right_c):
            temp2 = new_array[left_r][i+1]
            new_array[left_r][i+1] = temp1
            temp1 = temp2

        for i in range(left_r, right_r):
            temp2 = new_array[i+1][right_c]
            new_array[i+1][right_c] = temp1
            temp1 = temp2

        for i in range(right_c - left_c):
            temp2 = new_array[right_r][right_c-i-1]
            new_array[right_r][right_c-i-1] = temp1
            temp1 = temp2

        for i in range(right_r - left_r):
            temp2 = new_array[right_r-i-1][left_c]
            new_array[right_r-i-1][left_c] = temp1
            temp1 = temp2

        left_r += 1
        left_c += 1
        right_r -= 1
        right_c -= 1


op = []         # 연산자
result = 17406
for i in range(K):
    r, c, s = map(int, r_input().split())         # 회전 연산의 정보
    op.append([r, c, s])

for oper in permutations([i for i in range(1, K+1)], K):
    new_array = {}
    for t in array:
        new_array[t] = [] + array[t]

    for ind in oper:
        r, c, s = op[ind-1][0], op[ind-1][1], op[ind-1][2]
        turn(r-s, c-s, r+s, c+s)

    for t in new_array:
        result = min(result, sum(new_array[t]))

print(result)

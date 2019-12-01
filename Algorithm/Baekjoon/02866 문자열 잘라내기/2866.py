# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

R, C = map(int, r_input().split())

words = ['' for _ in range(C)]      # 이분 탐색 후 남은 문자열

for i in range(R):
    input_word = r_input().rstrip()

    for j in range(C):
        words[j] += input_word[j]

save = ['' for _ in range(C)]
result = len(words[0])
ind = result // 2
flag = 0            # 0: save에 남아있는 문자열들이 중복이 아닌 경우, 1: save에 남아있는 문자열들 중 중복이 있는 경우

while True:
    if flag:
        flag = 0
        for i in range(C):
            tmp = save[i][ind:] + words[i]

            if tmp in words:
                flag = 1

            save[i] = save[i][:ind]
            words[i] = tmp

    else:
        for i in range(C):
            tmp = words[i][ind:]

            if tmp in words:
                flag = 1
            save[i] = words[i][:ind]
            words[i] = tmp

    if len(save[0]) == 0:
        break

    if flag:
        ind = len(save[0]) // 2

    else:
        ind = len(words[0]) // 2

print(result - len(words[0]))

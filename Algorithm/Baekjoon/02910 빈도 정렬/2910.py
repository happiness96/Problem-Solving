# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# N개의 숫자로 이루어져있고, 숫자는 모두 C보다 작거나 같다
N, C = map(int, r_input().split())

num_list = {}

for num in map(int, r_input().rstrip().split()):        # 각 숫자들의 빈도수 체크
    if num in num_list:
        num_list[num] += 1

    else:
        num_list[num] = 1

frequency = {}
for num in num_list:                                # 빈도수별로 나누기
    if num_list[num] in frequency:
        frequency[num_list[num]].append(num)
    else:
        frequency[num_list[num]] = [num]

for f in sorted(frequency)[::-1]:
    for a in frequency[f]:
        print((str(a) + ' ') * f, end='')

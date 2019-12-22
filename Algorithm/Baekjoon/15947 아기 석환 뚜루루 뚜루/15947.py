# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 석환이가 부르는 노래의 N번째 단어는 무엇일까?
N = int(r_input())

repeat = N // 14
number = N % 14

if number == 1 or number == 13:
    print('baby')

elif number == 2 or number == 0:
    print('sukhwan')

elif number == 5:
    print('very')

elif number == 6:
    print('cute')

elif number == 9:
    print('in')

elif number == 10:
    print('bed')

else:
    ru_count = repeat + 1

    if number in [3, 7, 11]:
        ru_count += 1

    print('tu' + 'ru' * ru_count if ru_count < 5 else 'tu+ru*' + str(ru_count))

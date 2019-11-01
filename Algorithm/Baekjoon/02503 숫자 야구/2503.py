# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

N = int(r())        # 민혁이가 영수에게 질문한 횟수
possible_num = [str(number) for number in range(123, 988)]

for i in range(N):
    num, strike, ball = map(int, r().split())
    num = str(num)

    tank = []           # 임시 저장소

    while possible_num:         # 가능한 숫자를 계속 비교
        comp = possible_num.pop()
        comp_strike = comp_ball = 0

        for j in range(3):
            if num[j] in comp:
                ind = comp.index(num[j])
                if j == ind:
                    comp_strike += 1
                else:
                    comp_ball += 1

        if strike == comp_strike and ball == comp_ball:
            tank.append(comp)

    possible_num += tank

result = len(possible_num)

for t in possible_num:
    if '0' in t or t[0] == t[1] or t[1] == t[2] or t[0] == t[2]:        # 필터링 (숫자에 0이 들어가있거나 같은 숫자가 2개 이상 들어간 경우)
        result -=1

print(result)

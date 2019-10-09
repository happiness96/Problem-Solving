#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

T = int(r())        # 테스트 케이스 개수

result = {0:0}

for i in range(1, 80001):   # 80000까지 3의 배수 혹은 7의 배수의합을 result에 넣는다
    if i % 3 == 0 or i % 7 == 0:
        result[i] = result[i-1] + i
    else:
        result[i] = result[i-1]

for N in map(int, r().split()):
    print(result[N])

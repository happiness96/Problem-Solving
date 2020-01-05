# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

# 테스트 케이스의 개수
T = int(r_input())

for _ in range(T):
    # 수행할 함수
    p = r_input().rstrip()

    n = int(r_input())      # 배열에 들어있는 수
    array = r_input().rstrip()
    X = deque(list(map(str, array[1:-1].split(',')))) if n else deque()        # 배열

    reverse = 0
    error = 0

    for order in p:
        if order == 'R':
            reverse = abs(reverse - 1)

        else:
            if not X:
                error = 1
                break

            if reverse:
                X.pop()

            else:
                X.popleft()

    if reverse:
        X = reversed(X)

    if error:
        print('error')
    else:
        print('[' + ','.join(X) + ']')

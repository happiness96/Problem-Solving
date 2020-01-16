# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    # 극장 좌석의 개수
    N = int(r_input())

    seats = [0] * (N + 1)

    # VIP의 수
    M = int(r_input())

    for _ in range(M):
        vip = int(r_input())
        seats[vip] = 1

    fibo = [1, 1]
    for _ in range(2, 41):
        fibo.append(fibo[-1] + fibo[-2])

    cnt = 0
    result = 1
    
    for i in range(1, N + 1):
        if seats[i] == 0:
            cnt += 1
        else:
            result *= fibo[cnt]
            cnt = 0

    if cnt:
        result *= fibo[cnt]

    print(result)


if __name__ == '__main__':
    run()

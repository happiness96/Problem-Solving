# -*- encoding: utf-8 -*-

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        total = 0

        for _ in range(N):
            p, x = map(float, input().split())

            total += p * x

        print('#' + str(t), total)

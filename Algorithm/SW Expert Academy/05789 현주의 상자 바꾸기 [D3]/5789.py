# -*- encoding: utf-8 -*-

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N, Q = map(int, input().split())
        box = [0] * N

        for i in range(1, Q + 1):
            L, R = map(int, input().split())

            for ind in range(L - 1, R):
                box[ind] = i

        print('#' + str(t), *box)

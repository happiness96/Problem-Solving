# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

if __name__ == '__main__':
    N = int(r_input())
    cows = list(map(int, r_input().split()))

    for i in range(N):
        if cows[i:] == sorted(cows[i:]):
            print(i)
            break

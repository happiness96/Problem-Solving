# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

ind = 1             # Index of Set
while True:
    n = int(r_input())       # The number of stack

    if n == 0:
        break

    stack = list(map(int, r_input().split()))       # blocks stack
    avr = sum(stack) // n
    gap = 0

    for s in stack:
        gap += abs(avr - s)

    print('Set #' + str(ind))
    print('The minimum number of moves is ' + str(gap // 2) + '.')
    print()

    ind += 1

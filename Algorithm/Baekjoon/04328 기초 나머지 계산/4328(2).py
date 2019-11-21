# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

while True:
    # p를 m으로 나눈 수를 b진법으로 나타내어라
    s = r_input().rstrip()

    if s == '0':
        break

    b, p, m = map(str, s.split())
    b = int(b)

    num_p = int(p, b)
    num_m = int(m, b)

    mod = num_p % num_m

    if mod == 0:
        print(0)
        continue

    len_mod = 0
    while True:
        if mod < b ** len_mod:
            break

        len_mod += 1

    result = ''
    for i in range(1, len_mod+1):
        result += str(mod // (b ** (len_mod - i)))
        mod %= b ** (len_mod - i)

    print(result)

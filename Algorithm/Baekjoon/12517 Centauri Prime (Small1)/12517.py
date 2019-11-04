# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

T = int(r())        # The number of test case

for i in range(T):
    country = r().rstrip()          # The name of country
    rule = ''

    if country[-1] == 'y':
        rule = 'nobody'

    elif country[-1] in 'aeiou':
        rule = 'a queen'

    else:
        rule = 'a king'

    print('Case #' + str(i+1) + ': ' + country + ' is ruled by ' + rule + '.')

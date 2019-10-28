#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())            # The number of test case

for i in range(N):
    G = int(r())        # The number of guests
    guests = {}
    for g in map(int,r().split()):
        if g in guests:
            guests.pop(g)
        else:
            guests[g] = 0
    
    print('Case #' + str(i+1) + ': ' + str(list(guests.keys()).pop()))

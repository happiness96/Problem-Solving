#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

the_number_of_gits = {1:1, 2:4}

for i in range(3,1000001):
    the_number_of_gits[i] = i + 2 *the_number_of_gits[i-1] - the_number_of_gits[i-2]
    
while 1:
    n = int(r())
    
    if n == 0:
        break
    
    print(the_number_of_gits[n])

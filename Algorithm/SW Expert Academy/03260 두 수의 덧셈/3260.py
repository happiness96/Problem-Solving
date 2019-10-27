#-*- encoding: utf-8 -*-
T = int(input())
 
for i in range(T):
    A, B = map(int,input().split())
    print('#' + str(i+1), end=' ')
    print(A + B)

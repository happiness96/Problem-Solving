# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline

S = int(r_input())

Cow_Line = deque()
num = 1

for _ in range(S):
    c = r_input().rstrip()

    if c == 'A L':
        Cow_Line.appendleft(str(num))
        num +=1

    elif c == 'A R':
        Cow_Line.append(str(num))
        num += 1

    else:
        if c[2] == 'L':
            for _ in range(int(c[4:])):
                if Cow_Line:
                    Cow_Line.popleft()

        elif c[2] == 'R':
            for _ in range(int(c[4:])):
                if Cow_Line:
                    Cow_Line.pop()

print('\n'.join(Cow_Line))

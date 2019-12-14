# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

hurted_finger = int(r_input())
limit = int(r_input())

if hurted_finger == 1:
    if limit == 0:
        print(0)
    else:
        print(8 * limit)

elif hurted_finger == 5:
    print(8 * limit + 4)

else:
    if limit % 2:
        print(8 * (limit // 2) + 9 - hurted_finger)

    else:
        print(8 * (limit // 2) + hurted_finger - 1)

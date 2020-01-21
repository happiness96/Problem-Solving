# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

if __name__ == '__main__':
    # 톱니바퀴의 개수
    T = int(r_input())

    gear = [r_input().rstrip() for _ in range(T)]

    K = int(r_input())

    for _ in range(K):
        n, rot = map(int, r_input().split())
        n -= 1

        turn_right = []
        turn_left = []

        if rot == 1:
            turn_right.append(n)

        else:
            turn_left.append(n)

        r = -rot

        for i in range(n, 0, -1):
            if gear[i][6] != gear[i - 1][2]:
                if r == 1:
                    turn_right.append(i - 1)

                else:
                    turn_left.append(i - 1)

                r = -r

            else:
                break

        r = -rot

        for i in range(n, T - 1):
            if gear[i][2] != gear[i + 1][6]:
                if r == 1:
                    turn_right.append(i + 1)

                else:
                    turn_left.append(i + 1)

                r = -r

            else:
                break

        for right in turn_right:
            gear[right] = gear[right][-1] + gear[right][:-1]

        for left in turn_left:
            gear[left] = gear[left][1:] + gear[left][0]

    result = 0

    for g in gear:
        if g[0] == '1':
            result += 1

    print(result)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def swap(ele):
    if ele == '0':
        return '1'
    else:
        return '0'


def run():
    N = int(r_input())
    start1 = list(r_input().rstrip())
    start2 = []
    end = list(r_input().rstrip())

    if start1 == end:
        print(0)
        exit()

    if N == 2:
        if start1[0] != end[0] and start1[1] != end[1]:
            print(1)
        else:
            print(-1)
        exit()

    start2.append(swap(start1[0]))
    start2.append(swap(start1[1]))

    start2.extend(start1[2:])

    cnt1 = 0
    cnt2 = 1

    for i in range(1, N - 1):
        if start1[i - 1] != end[i - 1]:
            for j in range(i - 1, i + 2):
                start1[j] = swap(start1[j])
            cnt1 += 1

        if start2[i - 1] != end[i - 1]:
            for j in range(i - 1, i + 2):
                start2[j] = swap(start2[j])
            cnt2 += 1

    if start1[-1] != end[-1] and start1[-2] != end[-2]:
        start1[-1] = swap(start1[-1])
        start1[-2] = swap(start1[-2])
        cnt1 += 1

    if start2[-1] != end[-1] and start2[-2] != end[-2]:
        start2[-1] = swap(start2[-1])
        start2[-2] = swap(start2[-2])
        cnt2 += 1

    result = -1

    if start1 == end:
        result = cnt1

    if start2 == end:
        if result == -1:
            result = cnt2

        else:
            result = min(result, cnt2)

    print(result)


if __name__ == '__main__':
    run()

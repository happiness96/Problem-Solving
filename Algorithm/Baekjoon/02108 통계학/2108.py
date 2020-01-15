# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def run():
    N = int(r_input())

    numbers = {}
    total = 0
    maxi = 0
    maxi_list = []

    for _ in range(N):
        num = int(r_input())

        total += num

        if num not in numbers:
            numbers[num] = 0

        numbers[num] += 1

        if numbers[num] > maxi:
            maxi = numbers[num]
            maxi_list = [num]

        elif numbers[num] == maxi:
            maxi_list.append(num)

    print(round(total / N))

    cut = N // 2 + 1

    t = 0
    for node in sorted(numbers):
        t += numbers[node]
        if t >= cut:
            print(node)
            break

    if len(maxi_list) > 1:
        print(sorted(maxi_list)[1])
    else:
        print(maxi_list[0])

    print(max(numbers) - min(numbers))


if __name__ == '__main__':
    run()

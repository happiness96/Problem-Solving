# -*- encoding: utf-8 -*-
import sys
from itertools import combinations
r_input = sys.stdin.readline

# 임의의 카드 6장
cards = list(map(str, r_input().rstrip().split(',')))
queue = []

for case in combinations(list(range(6)), 2):
    queue.append(cards[case[0]] + cards[case[1]])


def get_number(num):
    if num in 'abcdef':
        return ord(num) - 87
    else:
        return int(num)


def sorting_with_lower_number(group):           # 작은 수가 큰 순서대로
    lower_number_group = {}

    for g in group:
        lower_number = min(get_number(g[0]), get_number(g[2]))

        if lower_number not in lower_number_group:
            lower_number_group[lower_number] = []

        lower_number_group[lower_number].append(g)

    for n in sorted(lower_number_group, reverse=True):
        if len(lower_number_group[n]) == 2:
            card1 = lower_number_group[n][0]
            card2 = lower_number_group[n][1]

            num1 = get_number(card1[0])
            num2 = get_number(card1[2])

            if num1 > num2:
                if card1[1] == 'b':
                    print(card1)
                    print(card2)
                else:
                    print(card2)
                    print(card1)

            else:
                if card1[3] == 'b':
                    print(card1)
                    print(card2)
                else:
                    print(card2)
                    print(card1)

        else:
            print(lower_number_group[n][0])


def sorting_with_biger_number(group):           # 큰 수가 큰 순서대로
    biger_number_group = {}       # 큰 수

    for g in group:
        biger_number = max(get_number(g[0]), get_number(g[2]))

        if biger_number not in biger_number_group:
            biger_number_group[biger_number] = []

        biger_number_group[biger_number].append(g)

    for n in sorted(biger_number_group, reverse=True):
        # print(biger_number_group[n])
        sorting_with_lower_number(biger_number_group[n])


def sorting_with_color(group):
    # 색이 같은 쌍인지
    same_color = []
    other_color = []

    for g in group:
        if g[1] == g[3]:
            same_color.append(g)
        else:
            other_color.append(g)

    sorting_with_biger_number(same_color)
    sorting_with_biger_number(other_color)


def sorting():
    group1 = []         # 연속된 수
    group2 = []         # 같은 수
    group3 = []         # 그 외

    for q in queue:
        num1 = get_number(q[0])
        num2 = get_number(q[2])

        if abs(num1 - num2) == 1 or (num1, num2) in [(1, 15), (15, 1)]:
            group1.append(q)

        elif num1 == num2:
            group2.append(q)

        else:
            group3.append(q)

    sorting_with_color(group1)
    sorting_with_color(group2)
    sorting_with_color(group3)


sorting()

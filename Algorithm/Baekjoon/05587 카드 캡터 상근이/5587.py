# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

n = int(r_input())

tmp = 2 * n + 1

# 상근이의 카드
s_cards = [0] * tmp
# 근상이의 카드
g_cards = [0] + [1] * (2 * n)

for _ in range(n):
    c = int(r_input())
    s_cards[c] = 1
    g_cards[c] = 0


def game_start():
    game_over = [0] * tmp
    up = 0

    turn = 0        # 0: 상근이 차례, 1: 근상이 차례

    while s_cards != game_over and g_cards != game_over:
        if not turn:
            flag = 0

            for i in range(up + 1, tmp):
                if s_cards[i]:
                    s_cards[i] = 0
                    up = i
                    flag = 1
                    break

        else:
            flag = 0

            for i in range(up + 1, tmp):
                if g_cards[i]:
                    g_cards[i] = 0
                    up = i
                    flag = 1
                    break

        turn = abs(turn - 1)

        if not flag:
            up = 0


game_start()

print(g_cards.count(1))
print(s_cards.count(1))

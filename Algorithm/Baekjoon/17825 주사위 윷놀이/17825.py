import sys
r_input = sys.stdin.readline
sys.setrecursionlimit(10**6)

die = list(map(int, r_input().split()))         # 10개의 주사위

board = [i * 2 for i in range(21)]          # ind: 0(시작) ~ 20 (40)
board1 = [10, 13, 16, 19]               # ind: 5, 21 ~ 23, 50
board2 = [20, 22, 24]                   # ind: 10, 31 ~ 32, 50
board3 = [30, 28, 27, 26]               # ind: 15, 41 ~ 43, 50
board4 = [25, 30, 35]                   # ind: 50 ~ 52, 20

result = 0
location = [0, 0, 0, 0]


def rolling_die(num, total):
    global result

    if num == 10:               # 주사위 10개를 다 돌렸다면
        if total > result:
            result = total
        return

    loop = location.index(0) + 1 if 0 in location else 4

    for i in range(loop):
        if location[i] < 0:         # 말이 이미 판을 다 돌고 나간 상태
            continue

        tmp1 = location[i]
        plus = 0

        if tmp1 == 5 or 21 <= tmp1 <= 23:
            if tmp1 == 5:
                tmp2 = 20
            else:
                tmp2 = tmp1

            tmp2 += die[num]

            if tmp2 <= 23:
                if tmp2 in location:
                    continue

                plus = board1[tmp2 - 20]
                total += plus
                location[i] = tmp2

            elif tmp2 == 28:
                location[i] = -1

            else:
                tmp2 += 26

                if tmp2 == 53:
                    tmp2 = 20

                    if tmp2 in location:
                        continue

                    plus = board[20]
                    total += plus
                    location[i] = 20

                else:
                    if tmp2 in location:
                        continue

                    plus = board4[tmp2 - 50]
                    total += plus
                    location[i] = tmp2

        elif tmp1 == 10 or 31 <= tmp1 <= 32:
            if tmp1 == 10:
                tmp2 = 30
            else:
                tmp2 = tmp1

            tmp2 += die[num]

            if tmp2 == 37:
                location[i] = -1

            elif tmp2 <= 32:
                if tmp2 in location:
                    continue

                plus = board2[tmp2 - 30]
                total += plus
                location[i] = tmp2

            else:
                tmp2 += 17

                if tmp2 == 53:
                    tmp2 = 20

                    if tmp2 in location:
                        continue

                    plus = board[20]
                    total += plus
                    location[i] = 20

                else:
                    if tmp2 in location:
                        continue

                    plus = board4[tmp2 - 50]
                    total += plus
                    location[i] = tmp2

        elif tmp1 == 15 or 41 <= tmp1 <= 43:
            if tmp1 == 15:
                tmp2 = 40
            else:
                tmp2 = tmp1

            tmp2 += die[num]

            if tmp2 == 48:
                location[i] = -1

            elif tmp2 <= 43:
                if tmp2 in location:
                    continue

                plus = board3[tmp2 - 40]
                total += plus
                location[i] = tmp2

            else:
                tmp2 += 6

                if tmp2 == 53:
                    tmp2 = 20

                    if tmp2 in location:
                        continue

                    plus = board[20]
                    total += plus
                    location[i] = 20

                else:
                    if tmp2 in location:
                        continue

                    plus = board4[tmp2 - 50]
                    total += plus
                    location[i] = tmp2

        elif tmp1 >= 50:
            tmp2 = tmp1 + die[num]

            if tmp2 > 53:
                location[i] = -1

            elif tmp2 == 53:
                tmp2 = 20

                if tmp2 in location:
                    continue

                location[i] = 20
                plus = board[20]
                total += plus

            else:
                if tmp2 in location:
                    continue

                location[i] = tmp2
                plus = board4[tmp2 - 50]
                total += plus

        else:
            tmp2 = tmp1 + die[num]

            if tmp2 in location:
                continue

            if tmp2 > 20:
                location[i] = -1

            else:
                location[i] = tmp2
                plus = board[tmp2]
                total += plus

        rolling_die(num + 1, total)

        location[i] = tmp1
        total -= plus


rolling_die(0, 0)

print(result)

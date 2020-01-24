# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, r_input().split())

    board = [list(map(int, r_input().split())) for _ in range(N)]

    horse = {}
    horse_status = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(1, K + 1):
        r, c, d = map(int, r_input().split())
        r -= 1
        c -= 1
        horse[i] = (r, c, d)
        horse_status[r][c].append(i)

    turn = 1

    while turn <= 1000:
        for i in range(1, K + 1):
            if horse_status[horse[i][0]][horse[i][1]][0] != i:
                continue

            horse_row = horse[i][0]
            horse_col = horse[i][1]
            horse_dir = horse[i][2]

            horses = horse_status[horse_row][horse_col]
            horse_status[horse_row][horse_col] = []

            if horse_dir == 1:        # 오른쪽
                horse_col += 1
            elif horse_dir == 2:      # 왼쪽
                horse_col -= 1
            elif horse_dir == 3:      # 위쪽
                horse_row -= 1
            else:                       # 아래쪽
                horse_row += 1

            horses.pop(0)
            reverse = 0
            # 파란색 타일
            if not 0 <= horse_row < N or not 0 <= horse_col < N or board[horse_row][horse_col] == 2:
                if horse_dir == 1:
                    horse_col -= 2
                    horse_dir = 2
                elif horse_dir == 2:
                    horse_col += 2
                    horse_dir = 1
                elif horse_dir == 3:
                    horse_row += 2
                    horse_dir = 4
                else:
                    horse_row -= 2
                    horse_dir = 3

                if not 0 <= horse_row < N or not 0 <= horse_col < N or board[horse_row][horse_col] == 2:
                    if horse_dir == 1:
                        horse_col -= 1
                    elif horse_dir == 2:
                        horse_col += 1
                    elif horse_dir == 3:
                        horse_row += 1
                    else:
                        horse_row -= 1

                elif board[horse_row][horse_col] == 1:  # 빨간색 타일
                    horses = horses[::-1]
                    reverse = 1

            elif board[horse_row][horse_col] == 1:          # 빨간색 타일
                horses = horses[::-1]
                reverse = 1

            if reverse:
                horses.append(i)
            else:
                horses = [i] + horses

            horse_status[horse_row][horse_col].extend(horses)

            if len(horse_status[horse_row][horse_col]) > 3:
                print(turn)
                exit()

            horse[i] = (horse_row, horse_col, horse_dir)

            for h in horses:
                horse[h] = (horse_row, horse_col, horse[h][2])

        turn += 1

    print(-1)

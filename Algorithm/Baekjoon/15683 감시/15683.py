# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, r_input().split())          # 사무실의 세로, 가로 크기

office = {}             # 사무실 각 칸의 정보
cameras = []            # 카메라 정보 저장

for i in range(N):
    office[i] = list(r_input().rstrip().split())           # 사무실 각 칸의 정보 입력

for i in range(N):
    for j in range(M):
        if office[i][j] in '1234':
            cameras.append([i, j, office[i][j]])
            continue
        
        if office[i][j] == '5':       # 5번 감시 카메라
            for a in range(i-1, -1, -1):        # 위쪽 방향
                if office[a][j] == '6':
                    break

                if office[a][j] == '0':
                    office[a][j] = '#'

            for a in range(j-1, -1, -1):        # 왼쪽 방향            
                if office[i][a] == '6':
                    break

                if office[i][a] == '0':
                    office[i][a] = '#'

            for a in range(i + 1, N):           # 아래쪽 방향
                if office[a][j] == '6':
                    break

                if office[a][j] == '0':
                    office[a][j] = '#'

            for a in range(j+1, M):             # 오른쪽 방향
                if office[i][a] == '6':
                    break

                if office[i][a] == '0':
                    office[i][a] = '#'


blind_spot = 0          # 최소 사각 지대
len_camera = len(cameras)       # 카메라의 개수

for i in range(N):
    blind_spot += ''.join(office[i]).count('0')


def find_blind_spot(ind):             # 최소 사각 지대 찾기
    if ind == len_camera:           # 모든 카메라를 다 탐색한 경우
        global blind_spot

        comp_blind_spot = 0
        for i in range(N):
            comp_blind_spot += ''.join(office[i]).count('0')
        blind_spot = min(blind_spot, comp_blind_spot)

        if blind_spot == 0:
            print(0)
            exit()

        return

    row = cameras[ind][0]           # 카메라의 위치
    col = cameras[ind][1]
    num = cameras[ind][2]           # 카메라 타입

    if num == '1':                # 1번 카메라
        temp = []
        for a in range(row-1, -1, -1):           # 위쪽 방향
            if office[a][col] == '6':
                break
            if office[a][col] == '0':
                temp.append(a)
                office[a][col] = '#'

        find_blind_spot(ind + 1)

        while temp:
            c = temp.pop()
            office[c][col] = '0'

        for a in range(col-1, -1, -1):          # 왼쪽 방향
            if office[row][a] == '6':
                break
            if office[row][a] == '0':
                temp.append(a)
                office[row][a] = '#'

        find_blind_spot(ind + 1)

        while temp:
            c = temp.pop()
            office[row][c] = '0'

        for a in range(row + 1, N):             # 아래쪽 방향
            if office[a][col] == '6':
                break
            if office[a][col] == '0':
                temp.append(a)
                office[a][col] = '#'

        find_blind_spot(ind + 1)

        while temp:
            c = temp.pop()
            office[c][col] = '0'

        for a in range(col + 1, M):             # 오른쪽 방향
            if office[row][a] == '6':
                break
            if office[row][a] == '0':
                temp.append(a)
                office[row][a] = '#'

        find_blind_spot(ind + 1)

        while temp:
            c = temp.pop()
            office[row][c] = '0'

    elif num == '2':              # 2번 카메라
        temp = []

        for a in range(col-1, -1, -1):          # 왼쪽 방향
            if office[row][a] == '6':
                break
            if office[row][a] == '0':
                temp.append(a)
                office[row][a] = '#'

        for a in range(col + 1, M):             # 오른쪽 방향
            if office[row][a] == '6':
                break
            if office[row][a] == '0':
                temp.append(a)
                office[row][a] = '#'

        find_blind_spot(ind + 1)

        while temp:
            c = temp.pop()
            office[row][c] = '0'

        for a in range(row-1, -1, -1):           # 위쪽 방향
            if office[a][col] == '6':
                break
            if office[a][col] == '0':
                temp.append(a)
                office[a][col] = '#'

        for a in range(row + 1, N):             # 아래쪽 방향
            if office[a][col] == '6':
                break
            if office[a][col] == '0':
                temp.append(a)
                office[a][col] = '#'

        find_blind_spot(ind + 1)

        while temp:
            c = temp.pop()
            office[c][col] = '0'

    elif num == '3':              # 3번 카메라
        left_temp = []
        right_temp = []
        up_temp = []
        down_temp = []

        for a in range(col-1, -1, -1):          # 왼쪽 방향
            if office[row][a] == '6':
                break
            if office[row][a] == '0':
                left_temp.append(a)
                office[row][a] = '#'

        for a in range(row-1, -1, -1):           # 위쪽 방향
            if office[a][col] == '6':
                break
            if office[a][col] == '0':
                up_temp.append(a)
                office[a][col] = '#'

        find_blind_spot(ind + 1)

        while left_temp:
            c = left_temp.pop()
            office[row][c] = '0'

        for a in range(col + 1, M):             # 오른쪽 방향
            if office[row][a] == '6':
                break
            if office[row][a] == '0':
                right_temp.append(a)
                office[row][a] = '#'

        find_blind_spot(ind + 1)

        while up_temp:
            c = up_temp.pop()
            office[c][col] = '0'

        for a in range(row + 1, N):             # 아래쪽 방향
            if office[a][col] == '6':
                break
            if office[a][col] == '0':
                down_temp.append(a)
                office[a][col] = '#'

        find_blind_spot(ind + 1)

        while right_temp:
            c = right_temp.pop()
            office[row][c] = '0'

        for a in range(col-1, -1, -1):          # 왼쪽 방향
            if office[row][a] == '6':
                break
            if office[row][a] == '0':
                left_temp.append(a)
                office[row][a] = '#'

        find_blind_spot(ind + 1)

        while down_temp:
            c = down_temp.pop()
            office[c][col] = '0'

        while left_temp:
            c = left_temp.pop()
            office[row][c] = '0'

    elif num == '4':              # 4번 카메라
        left_temp = []
        right_temp = []
        up_temp = []
        down_temp = []

        for a in range(col - 1, -1, -1):  # 왼쪽 방향
            if office[row][a] == '6':
                break
            if office[row][a] == '0':
                left_temp.append(a)
                office[row][a] = '#'

        for a in range(row - 1, -1, -1):  # 위쪽 방향
            if office[a][col] == '6':
                break
            if office[a][col] == '0':
                up_temp.append(a)
                office[a][col] = '#'

        for a in range(col + 1, M):             # 오른쪽 방향
            if office[row][a] == '6':
                break
            if office[row][a] == '0':
                right_temp.append(a)
                office[row][a] = '#'

        find_blind_spot(ind + 1)

        while left_temp:
            c = left_temp.pop()
            office[row][c] = '0'

        for a in range(row + 1, N):             # 아래쪽 방향
            if office[a][col] == '6':
                break
            if office[a][col] == '0':
                down_temp.append(a)
                office[a][col] = '#'

        find_blind_spot(ind + 1)

        while up_temp:
            c = up_temp.pop()
            office[c][col] = '0'

        for a in range(col - 1, -1, -1):  # 왼쪽 방향
            if office[row][a] == '6':
                break
            if office[row][a] == '0':
                left_temp.append(a)
                office[row][a] = '#'

        find_blind_spot(ind + 1)

        while right_temp:
            c = right_temp.pop()
            office[row][c] = '0'

        for a in range(row - 1, -1, -1):  # 위쪽 방향
            if office[a][col] == '6':
                break
            if office[a][col] == '0':
                up_temp.append(a)
                office[a][col] = '#'

        find_blind_spot(ind + 1)

        while up_temp:
            c = up_temp.pop()
            office[c][col] = '0'

        while left_temp:
            c = left_temp.pop()
            office[row][c] = '0'

        while down_temp:
            c = down_temp.pop()
            office[c][col] = '0'


find_blind_spot(0)

print(blind_spot)

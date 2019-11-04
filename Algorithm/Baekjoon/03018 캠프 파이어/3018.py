# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

N = int(r())        # MT에 참가한 사람의 수
E = int(r())        # MT 기간

songs = {}
songs_num = 0       # 곡의 개수

for i in range(1, N+1):
    songs[i] = []

for i in range(E):
    part = list(map(int, r().split()))[1:]

    if 1 in part:           # 선영이가 MT에 참석한  경우
        for c in songs:
            if c in part:       # 참가한 사람들
                songs[c].append(1)
            else:               # 참가하지 않은 사람들
                songs[c].append(0)
        songs_num += 1

    else:
        temp = [0] * songs_num      # 공유할 임시 저장소
        for c in part:
            for t in range(songs_num):
                if songs[c][t] == 1:     # 배운 노래라면 공유하기
                    temp[t] = 1

        for c in part:          # copy
            for j in range(songs_num):
                songs[c][j] = temp[j]


for i in range(1, N+1):
    if songs[i] == [1] * songs_num:
        print(i)

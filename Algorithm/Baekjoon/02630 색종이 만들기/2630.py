#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # 종이의 한 변의 길이
paper = {}          # 종이
white = blue = 0        # 하얀색, 파란색으로 칠해진 칸의 개수

for i in range(N):
    paper[i] = list(map(int, r().split()))

def find_paper(start_r, start_w, length):
    global white, blue
    
    if length == 1:             # 한 칸인 경우
        if paper[start_r][start_w] == 1:
            blue += 1
        else:
            white += 1
    
    else:
        temp = paper[start_r][start_w]
        conti = 0
        for i in range(start_r, start_r + length):
            for j in range(start_w, start_w + length):
                if paper[i][j] != temp:
                    conti = 1
                    break
            if conti:
                break
                    
        if conti:
            length //= 2
            find_paper(start_r, start_w, length)
            find_paper(start_r + length, start_w, length)
            find_paper(start_r, start_w + length, length)
            find_paper(start_r + length, start_w + length, length)
        
        else:
            if temp: blue +=1
            else: white += 1

find_paper(0, 0, N)

print(white)
print(blue)

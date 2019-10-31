#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

width, height = map(int, r().split())        # width: 가로길이, height: 세로길이

n = int(r())        # 칼로 잘라야하는 점선의 개수

maxi = 0            # 최대 넓이

x = [0, width]             # 세로로 자르는 점선 번호
y = [0, height]             # 가로로 자르는 점선 번호

for i in range(n):
    a, b = map(int, r().split())
    
    if a:
        x.append(b)
    else:
        y.append(b)

x.sort()
y.sort()

for i in range(1, len(x)):
    for j in range(1, len(y)):
        area = (x[i] - x[i-1]) * (y[j] - y[j-1])
        maxi = max(maxi, area)

print(maxi)

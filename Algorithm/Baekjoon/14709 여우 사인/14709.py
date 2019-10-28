#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())            # 손가락이 닿아있는 쌍의 개수

fingers = [[], [], [], [], []]

result = 0

for i in range(N):
    a,b = map(int, r().split())     # 서로 맛닿아있는 두 손가락
    if a > b:
        a, b = b, a
    fingers[a].append(b)
    
# 세 손가락이 맛닿아있는지 확인
if 3 in fingers[1] and 4 in fingers[1] and 4 in fingers[3]:
    result = 1

# 두 번째, 다섯 번째 손가락이 떨어져 있는지 확인
if len(fingers[2]) > 0 or 2 in fingers[1]:
    result = 0
    
for i in range(1, 5):
    if 5 in fingers[i]:
        result = 0

print('Wa-pa-pa-pa-pa-pa-pow!' if result else 'Woof-meow-tweet-squeek')

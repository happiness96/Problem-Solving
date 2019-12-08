# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 영식이가 운동을 선택한다면 기존 맥박 X에서 T만큼 증가한다. 하지만 M을 넘을 수 없다.
# 휴식을 선택한다면 기존 맥박 X에서 R만큼 감소한다. 하지만 m보다 낮아질 수 없다.
# 영식이는 운동을 N분 하려한다.
# 처음 맥박은 m이다.
N, m, M, T, R = map(int, r_input().split())

# 운동을 1분이라도 했을 때 M을 넘어버리면 운동을 할 수 없다.
if m + T > M:
    print(-1)
    exit()

minutes = 0     # 소모된 시간
X = m           # 처음 맥박

while N:
    if X + T <= M:          # 운동을 했을 때 M을 넘지 않는다면
        N -= 1
        X += T
        minutes += 1
        
    else:                   # 휴식이 필요하다면
        X = max(X - R, m)       # 맥박은 m 밑으로 낮아질 수 없다.
        minutes += 1

print(minutes)

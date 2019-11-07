# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

N = int(r())        # 재현시의 크기 N x N
hyun = {}           # 재현시
total = 0           # 재현시의 인구 총합
result = 1777900      # 최소값

for i in range(N):
    hyun[i] = list(map(int,r().split()))
    total += sum(hyun[i])

for i in range(N-2):
    for j in range(1, N-1):
        x = i
        y = j

        for k in range(1, N):
            for l in range(1, N):
                d1 = k
                d2 = l

                if y-d1 < 0 or y+d2 >= N or x+d1+d2 >= N:
                    break

                one = 0     # 1번 선거구
                for a in range(x):
                    one += sum(hyun[a][:y+1])
                for a in range(d1):
                    one += sum(hyun[x+a][:y-a])

                two = 0     # 2번 선거구
                for a in range(x+1):
                    two += sum(hyun[a][y+1:])
                for a in range(d2):
                    two += sum(hyun[x+a+1][y+a+2:])

                three = 0   # 3번 선거구
                for a in range(d2):
                    three += sum(hyun[x+d1+a][:y-d1+a])
                for a in range(N-d1-d2-x):
                    three += sum(hyun[x+d1+d2+a][:y-d1+d2])

                four = 0    # 4번 선거구
                for a in range(d1):
                    four += sum(hyun[x+d2+a+1][y-d1+d2+(d1-a):])
                for a in range(N-d1-d2-x-1):
                    four += sum(hyun[x+d1+d2+a+1][y-d1+d2:])

                five = total-one-two-three-four     # 5번 선거구

                maximum = max(one, two, three, four, five)
                minimum = min(one, two, three, four, five)

                result = min(result, maximum - minimum)

                if result == 0:
                    print(result)
                    exit()

print(result)

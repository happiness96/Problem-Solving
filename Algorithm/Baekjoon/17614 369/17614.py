#-*- encoding: utf-8 -*-
N = int(input())
clap = 0        # 박수 친 횟수

for i in range(1, N+1):
    num = str(i)
    clap += num.count('3') + num.count('6') + num.count('9')

print(clap)

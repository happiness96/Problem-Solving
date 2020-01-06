# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 테스트 케이스의 개수
T = int(r_input())

fibo = {0: 0, 1: 1}

limit = 1000000000
ind = 2

while True:
    fibo[ind] = fibo[ind - 1] + fibo[ind - 2]

    if fibo[ind] > limit:
        break

    ind += 1

length = len(fibo)

for _ in range(T):
    n = int(r_input())

    queue = []
    flag = 0

    for i in range(length):
        if fibo[i] < n:
            queue.append([fibo[i]])

        elif fibo[i] == n:
            print(n)
            flag = 1
            break
        else:
            break

    if flag:
        continue

    while queue:
        for _ in range(len(queue)):
            tmp = queue.pop()
            total = sum(tmp)

            for i in range(length):
                if fibo[i] not in tmp:
                    save = total + fibo[i]

                    if save < n:
                        queue.append(tmp + [fibo[i]])

                    elif save == n:
                        print(*sorted(tmp + [fibo[i]]))
                        flag = 1
                        break
                    else:
                        break

            if flag:
                break

        if flag:
            break

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# E개의 러버덕을 가지고 있다.
# 다영이를 제외한 N명의 회원들
# 회원 i는 xi개 이상, yi개 이하의 인형만 받는다.
# 다영이는 정확히 P명에게 E개의 인형을 선물하려 한다.

N, P, E = map(int, r_input().split())
save = []

for _ in range(N):
    x, y = map(int, r_input().split())
    save.append([x, y])


def dfs(ind, chk, minimum, maximum):
    chk[ind] = 1
    minimum += save[ind][0]
    maximum += save[ind][1]

    cnt = chk.count(1)

    if cnt == P and minimum <= E <= maximum:
        result = [0] * N
        remain = E - minimum

        for i in range(N):
            if chk[i]:
                if remain == 0:
                    result[i] = save[i][0]

                if remain >= save[i][1] - save[i][0]:
                    result[i] = save[i][1]
                    remain -= save[i][1] - save[i][0]

                else:
                    result[i] = save[i][0] + remain
                    remain = 0

        for r in result:
            print(r, end=' ')
        exit()

    for i in range(ind + 1, N):
        dfs(i, chk, minimum, maximum)

    chk[ind] = 0
    minimum -= save[ind][0]
    maximum -= save[ind][1]


for n in range(N - P + 1):
    dfs(n, [0] * N, 0, 0)

print(-1)

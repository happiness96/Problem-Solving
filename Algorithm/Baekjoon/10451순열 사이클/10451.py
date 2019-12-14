# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

T = int(r_input())          # 테스트 케이스의 개수


def run():
    for _ in range(T):
        N = int(r_input())      # 순열의 크기
        A = [0] + list(map(int, r_input().split()))

        visit = [0] * (N + 1)
        cnt = 0         # 사이클의 개수

        for i in range(1, N + 1):
            if not visit[i]:
                stack = {i}
                node = i

                while not visit[node]:
                    visit[node] = 1

                    node = A[node]

                cnt += 1

        print(cnt)


run()

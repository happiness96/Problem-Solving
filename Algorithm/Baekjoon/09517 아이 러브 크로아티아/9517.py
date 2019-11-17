# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

K = int(r_input())      # 처음 폭탄을 들고 있는 사람의 번호

N = int(r_input())      # 질문의 개수

limit = 210         # 폭탄 제한시간
amount = 0          # 게임 진행 누적 시간

game_over = 0
for i in range(N):
    # T: 질문에 대답하기까지 걸린 시간, Z: 그 플레이어의 대답
    T, Z = map(str, r_input().rstrip().split())
    
    if game_over:           # 이미 게임이 종료된 경우
        continue
        
    amount += int(T)

    if amount >= limit:         # 폭탄 제한 시간이 다 됐다면
        game_over = 1
        continue

    if Z == 'T':                # 문제를 맞췄다면 다음 사람으로
        K += 1

        if K == 9:
            K = 1

print(K)

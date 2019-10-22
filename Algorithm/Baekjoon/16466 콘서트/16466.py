#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())            # 1차 티켓팅에서 팔린 티켓들의 수

tickets = {}            # 1차 티켓팅에서 팔린 티켓들

for ticket_num in map(int,r().split()):
    tickets[ticket_num] = 0

for i in range(1, 1000001):
    if not i in tickets:
        print(i)
        break

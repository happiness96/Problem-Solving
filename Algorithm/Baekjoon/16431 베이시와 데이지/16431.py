#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

B_r, B_c = map(int, r().split())        # 베시의 좌표
D_r, D_c = map(int, r().split())        # 데이지의 좌표
J_r, J_c = map(int, r().split())        # 존의 좌표

distance_D = abs(J_r - D_r) + abs(J_c - D_c)        # 데이시가 존에게 가는 데 걸리는 시간
distance_B = abs(J_r - B_r) + abs(J_c - B_c)        # 베시가 존에게 가는 데 걸리는 시간

distance_B -= min(abs(J_r - B_r), abs(J_c - B_c))

print('bessie' if distance_B < distance_D else 'daisy' if distance_B > distance_D else 'tie')

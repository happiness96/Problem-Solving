#-*- encoding: utf-8 -*-
import sys;r=sys.stdin.readline

N,r,c = map(int,r().split())        # N : 행렬 (NxN), r = 행, c = 열


def Z(map_N, node, row, column):
    if row == r and column == c:    # (r,c)에 있는 값을 찾으면 종료
        print(node)
        exit()
        
    map_N -= 1
    
    if map_N == 1:
        print(node + 2 * (r - row) + (c - column))
        exit()
        
    if r < row + 2**(map_N-1) and c < column + 2**(map_N-1):                    # 1사분면에 있는 경우
        Z(map_N, node + 4**(map_N-1)*0, row, column)
        
    elif r < row + 2**(map_N-1) and c >= column + 2**(map_N-1):                 # 2사분면에 있는 경우
        Z(map_N, node + 4**(map_N-1)*1, row, column + 2**(map_N-1))
        
    elif r >= row + 2**(map_N-1) and c < column + 2**(map_N-1):                 # 3사분면에 있는 경우
        Z(map_N, node + 4**(map_N-1)*2, row + 2**(map_N-1), column)
        
    else :                                                                      # 4사분면에 있는 경우
        Z(map_N, node + 4**(map_N-1)*3, row + 2**(map_N-1), column + 2**(map_N-1))

if N == 1:
    print(2 * r + c)
    exit()
    
if r < 2**(N-1) and c < 2**(N-1):         # r과 c가 1사분면에 있는 경우
    Z(N, 4**(N-1)*0, 0, 0)
    
elif r < 2**(N-1) and c >= 2**(N-1):         # r과 c가 2사분면에 있는 경우
    Z(N, 4**(N-1)*1, 0, 2**(N-1))
    
elif r >= 2**(N-1) and c < 2**(N-1):         # r과 c가 3사분면에 있는 경우
    Z(N, 4**(N-1)*2, 2**(N-1), 0)
    
else:                                      # r과 c가 4사분면에 있는 경우
    Z(N, 4**(N-1)*3, 2**(N-1), 2**(N-1))

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

dwarf = [int(r_input()) for tall in range(9)]         # 아홉 난쟁이의 키 입력받기
gap = sum(dwarf) - 100              # 일곱 난쟁이의 키와 아홉 난쟁이의 키의 차
dwarf.sort()

for i in range(9):                  # 브루트포스
    for j in range(i+1, 9):
        if dwarf[i] + dwarf[j] == gap:
            dwarf.pop(i)
            dwarf.pop(j-1)

            for d in dwarf:
                print(d)
            exit()

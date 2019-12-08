# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

finished_puzzle = ['ABCD', 'EFGH', 'IJKL', 'MNO']
scatter = 0

for i in range(4):
    puzzle = r_input().rstrip()
    for j in range(4):
        for k in range(4):
            if puzzle[j] in finished_puzzle[k]:
                scatter += abs(k - i) + abs(finished_puzzle[k].index(puzzle[j]) - j)

print(scatter)

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(r_input())          # 노드의 개수
tree = {}
level = {}
find_mother = [1] * N       # 1레벨 노드 찾기

for i in range(N):
    # num: 노드의 번호, left: 왼쪽 자식 노드, right: 오른쪽 자식 노드
    num, left, right = map(int, r_input().split())
    tree[num] = [left, right]
    
    # 부모가 있는 노드는 체크
    if left != -1:
        find_mother[left-1] = 0

    if right != -1:
        find_mother[right-1] = 0


def find_row(current_level, node):          # 현재 노드의 열 찾기(dfs)
    global row
    
    node_left = tree[node][0]
    node_right = tree[node][1]

    if node_left != -1:              # 현재 노드의 왼쪽 자식 노드가 없는 경우
        find_row(current_level+1, node_left)

    if current_level in level:
        level[current_level].append(row)

    else:
        level[current_level] = [row]

    row += 1

    if node_right != -1:             # 현재 노드의 오른쪽 자식 노드가 없는 경우
        find_row(current_level+1, node_right)


row = 1
find_row(1, find_mother.index(1) + 1)

result_level = 0            # 너비가 가장 넓은 레벨
result_width = 0            # 그 때의 너비

for l in sorted(level):
    width = level[l][-1] - level[l][0] + 1

    if width > result_width:
        result_level = l
        result_width = width

print(result_level, result_width)

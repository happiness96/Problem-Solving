# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 노드의 개수
N = int(r_input())
tree = {}

for _ in range(N):
    parent, left, right = map(str, r_input().rstrip().split())
    tree[parent] = [left, right]


def pre_order(node):         # 전위 순회
    print(node, end='')

    left_node = tree[node][0]
    right_node = tree[node][1]

    if not left_node == '.':
        pre_order(left_node)

    if not right_node == '.':
        pre_order(right_node)


def in_order(node):             # 중위 순회
    left_node = tree[node][0]
    right_node = tree[node][1]

    if not left_node == '.':
        in_order(left_node)

    print(node, end='')

    if not right_node == '.':
        in_order(right_node)


def post_order(node):           # 후위 순회
    left_node = tree[node][0]
    right_node = tree[node][1]

    if not left_node == '.':
        post_order(left_node)

    if not right_node == '.':
        post_order(right_node)

    print(node, end='')


pre_order('A')
print()
in_order('A')
print()
post_order('A')

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def find_leaf_node(node):
    global result

    is_leaf = 1
    
    for n in child[node]:
        if n not in delete_nodes:
            find_leaf_node(n)
            is_leaf = 0

    result += is_leaf


if __name__ == '__main__':
    N = int(r_input())

    A = list(map(int, r_input().split()))

    delete_node = int(r_input())

    child = {node: [] for node in range(N)}
    root = []

    for i in range(N):
        if A[i] != -1:
            child[A[i]].append(i)

        else:
            root.append(i)

    delete_nodes = [delete_node]
    queue = [delete_node]

    while queue:
        tmp = queue.pop()
        for n in child[tmp]:
            queue.append(n)
            delete_nodes.append(n)

    result = 0

    for node in root:
        if node not in delete_nodes:
            find_leaf_node(node)

    print(result)

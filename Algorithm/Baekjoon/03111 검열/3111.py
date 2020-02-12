# -*- encoding: utf-8 -*-
import sys
from collections import deque
r_input = sys.stdin.readline


def run():
    A = list(r_input().rstrip())
    rev_A = A[::-1]
    T = deque(list(r_input().rstrip()))

    len_A = len(A)

    front_queue = []
    end_queue = []

    turn = 0

    while T:
        if turn == 0:
            front_queue.append(T.popleft())

            if front_queue[-len_A:] == A:
                front_queue[-len_A:] = []
                turn = 1

        else:
            end_queue.append(T.pop())

            if end_queue[-len_A:] == rev_A:
                end_queue[-len_A:] =[]
                turn = 0

    while front_queue and end_queue:
        if turn == 0:
            front_queue.append(end_queue.pop())

            if front_queue[-len_A:] == A:
                front_queue[-len_A:] = []
                turn = 1

        else:
            end_queue.append(front_queue.pop())

            if end_queue[-len_A:] == rev_A:
                end_queue[-len_A:] =[]
                turn = 0

    print(''.join(front_queue) + ''.join(reversed(end_queue)))


if __name__ == '__main__':
    run()

# -*- encoding: utf-8 -*-
import sys
from heapq import *
r_input = sys.stdin.readline


def run():
    T = int(r_input())

    for _ in range(T):
        Q = int(r_input())

        max_heap = []
        min_heap = []

        del_max_heap = []
        del_min_heap = []

        for _ in range(Q):
            order, value = map(str, r_input().rstrip().split())

            value = int(value)

            if order == 'I':
                heappush(min_heap, value)
                heappush(max_heap, -value)

            else:
                if value == 1:  # 최댓값 삭제
                    if max_heap:
                        heappush(del_max_heap, -heappop(max_heap))

                else:  # 최솟값 삭제
                    if min_heap:
                        heappush(del_min_heap, -heappop(min_heap))

            while max_heap and del_min_heap and max_heap[0] == del_min_heap[0]:
                heappop(max_heap)
                heappop(del_min_heap)

            while min_heap and del_max_heap and min_heap[0] == del_max_heap[0]:
                heappop(min_heap)
                heappop(del_max_heap)

        if not max_heap:
            print('EMPTY')

        else:
            print(-max_heap[0], min_heap[0])


if __name__ == '__main__':
    run()

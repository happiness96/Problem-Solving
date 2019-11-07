# -*- encoding: utf-8 -*-
import sys
r = sys.stdin.readline

n, k = map(int, r().split())        # 합이 n이 되며 사전 순으로 k 번째에 오는 식
cnt = 0


def find_number(total, num_list):
    global cnt

    if total < n:
        find_number(total + 1, num_list + ['1'])
        find_number(total + 2, num_list + ['2'])
        find_number(total + 3, num_list + ['3'])

    if total == n:
        cnt += 1
        if cnt == k:
            print('+'.join(num_list))
            exit()


find_number(0, [])
print(-1)

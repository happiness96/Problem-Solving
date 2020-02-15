# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

if __name__ == '__main__':
    N = int(r_input())
    M = int(r_input())

    result = []

    recommend_count = {}

    for st_no in map(int, r_input().split()):
        if len(result) < N:
            if st_no in result:
                recommend_count[st_no] += 1

            else:
                recommend_count[st_no] = 1
                result.append(st_no)

        else:
            if st_no in result:
                recommend_count[st_no] += 1

            else:
                minimum = min(recommend_count.values())
                tmp = 0

                for number in result:
                    if recommend_count[number] == minimum:
                        tmp = number
                        break

                result.pop(result.index(tmp))
                result.append(st_no)

                recommend_count.pop(tmp)
                recommend_count[st_no] = 1

    print(*sorted(result))

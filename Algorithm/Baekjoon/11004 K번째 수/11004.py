# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

N, K = map(int, r_input().split())          # N: 숫자의 개수, K번째에 있는 수

numbers = sorted(map(int, r_input().split()))

print(numbers[K-1])

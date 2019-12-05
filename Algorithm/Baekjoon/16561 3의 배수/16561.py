import sys
r_input = sys.stdin.readline

n = int(r_input()) // 3
result = 0

for i in range(1, n - 1):
    result += i

print(result)

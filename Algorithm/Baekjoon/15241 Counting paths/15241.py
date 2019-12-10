import sys
r_input = sys.stdin.readline

N, M = map(int, r_input().split())

dp = [0] * M
dp[0] = 1

for _ in range(N):
    s = r_input().rstrip()
    if s[0] == 'X':
        dp[0] = 0

    for i in range(1, M):
        if s[i] == '.':
            dp[i] += dp[i - 1]

        else:
            dp[i] = 0

print(dp[-1] % 1000000007)

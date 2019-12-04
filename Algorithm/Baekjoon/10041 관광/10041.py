import sys
r_input = sys.stdin.readline

# W: 남북방향 도로의 개수, H: 동서방향 도로의 개수, N: 관광지의 개수
W, H, N = map(int, r_input().split())

X, Y = map(int, r_input().split())
cnt = 0

for _ in range(N - 1):
    a, b = map(int, r_input().split())

    if a > X and b > Y:
        tmp = min(a - X, b - Y)
        cnt += tmp

        X += tmp
        Y += tmp

        tmp = max(a - X, b - Y)
        cnt += tmp

    elif a < X and b < Y:
        tmp = min(X - a, Y - b)
        cnt += tmp

        X -= tmp
        Y -= tmp

        tmp = max(X - a, Y - b)
        cnt += tmp

    else:
        cnt += abs(a - X) + abs(b - Y)

    X = a
    Y = b

print(cnt)

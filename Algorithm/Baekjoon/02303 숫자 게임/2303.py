import sys
r_input = sys.stdin.readline

N = int(r_input())      # 사람의 수

maxi = 0
num = 0

for No in range(1, N + 1):
    cards = list(map(int, r_input().split()))

    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                total = cards[i] + cards[j] + cards[k]
                tmp = total % 10
                if tmp >= maxi:
                    maxi = tmp
                    num = No

print(num)

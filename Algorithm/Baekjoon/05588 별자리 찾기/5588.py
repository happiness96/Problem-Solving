import sys
r_input = sys.stdin.readline

m = int(r_input())      # 찾고자하는 별의 개수

start_x, start_y = map(int, r_input().split())

stars = set()          # 찾고자하는 별들

for _ in range(m - 1):
    x, y = map(int, r_input().split())

    stars.add((x - start_x, y - start_y))

n = int(r_input())      # 사진 속 별의 개수

pic_stars = set()

for _ in range(n):
    x, y = map(int, r_input().split())
    pic_stars.add((x, y))

for s in pic_stars:
    flag = 1

    for gap in stars:
        if (s[0] + gap[0], s[1] + gap[1]) not in pic_stars:
            flag = 0
            break

    if flag:
        print(s[0] - start_x, s[1] - start_y)
        break

import sys
r_input = sys.stdin.readline

T = int(r_input())      # 테스트 케이스의 개수

for _ in range(T):
    cry = list(map(str, r_input().rstrip().split()))
    not_fox_crying = []

    while True:
        s = r_input().rstrip()

        if s == 'what does the fox say?':
            break

        s_l = list(map(str, s.split()))
        not_fox_crying.append(s_l[2])

    for c in cry:
        if c not in not_fox_crying:
            print(c, end=' ')

# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

s = list(r_input().rstrip().rstrip())
total_score = 0
frame = 1
cnt = 1

score = {'S': 10, '-': 0}
for i in range(1, 10):
    score[str(i)] = i

for i in range(len(s)):
    if frame < 10:
        if s[i] == 'S':
            total_score += 10

            if s[i+2] == 'P':
                total_score += 10
            else:
                total_score += score[s[i + 1]] + score[s[i + 2]]

            frame += 1

        else:
            if cnt == 1:
                total_score += score[s[i]]
                cnt += 1

            else:
                if s[i] == 'P':
                    total_score += 10 - score[s[i - 1]]
                    total_score += score[s[i + 1]]

                else:
                    total_score += score[s[i]]
                cnt = 1
                frame += 1

    else:
        if s[i] == 'P':
            total_score += 10 - score[s[i - 1]]
        else:
            total_score += score[s[i]]

print(total_score)

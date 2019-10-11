#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

# A: the number of players in team A
# B: the number of players in team B
# G: the number of goals scored in the match
A, B, G = map(int, r().split())

players_in_A = list(r().rstrip().split())       # The names of players in team A
players_in_B = list(r().rstrip().split())       # The names of players in team A
players_who_scored = list(r().rstrip().split())     # The names of players who scored

score_A = 0         # Team A score
score_B = 0         # Team B score

for goal in players_who_scored:
    if goal in players_in_A:
        score_A += 1
    elif goal in players_in_B:
        score_B += 1

print('A' if score_A > score_B else 'B' if score_B > score_A else 'TIE')

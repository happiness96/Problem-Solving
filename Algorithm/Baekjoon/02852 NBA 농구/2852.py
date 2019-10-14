#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

N = int(r())        # 골이 들어간 횟수

team_one_score = 0      # 1팀 점수
team_two_score = 0      # 2팀 점수

team_one_minutes = 0        # 1팀이 이기고 있는 시간(분)
team_two_minutes = 0        # 2팀이 이기고 있는 시간(분)

team_one_seconds = 0        # 1팀이 이기고 있는 시간(초)
team_two_seconds = 0        # 2팀이 이기고 있는 시간(초)

last_goal_minutes = 0       # 마지막 골 시점(분)
last_goal_seconds = 0       # 마지막 골 시점(초)


def calculate_time(time_par):
    v_min, v_sec = map(int, time_par.split(':'))
    
    global team_one_minutes, team_two_minutes, team_one_seconds, team_two_seconds, last_goal_minutes, last_goal_seconds
    
    if team_one_score > team_two_score:         # 1팀이 이기고 있었을 경우
        team_one_minutes += v_min - last_goal_minutes
        team_one_seconds += v_sec - last_goal_seconds
        
        if team_one_seconds > 59:
            team_one_minutes += 1
            team_one_seconds -= 60
        
        if team_one_seconds < 0:
            team_one_minutes -= 1
            team_one_seconds += 60
            
    elif team_two_score > team_one_score:         # 2팀이 이기고 있었을 경우
        team_two_minutes += v_min - last_goal_minutes
        team_two_seconds += v_sec - last_goal_seconds
        
        if team_two_seconds > 59:
            team_two_minutes += 1
            team_two_seconds -= 60
        
        if team_two_seconds < 0:
            team_two_minutes -= 1
            team_two_seconds += 60
            
    last_goal_minutes = v_min
    last_goal_seconds = v_sec
    

for i in range(N):
    winner, time = map(str, r().rstrip().split())
    
    if winner == '1':
        calculate_time(time)
        team_one_score += 1
    else:
        calculate_time(time)
        team_two_score += 1

calculate_time('48:00')         # Time over

print('%02d'%team_one_minutes + ':' + '%02d'%team_one_seconds)
print('%02d'%team_two_minutes + ':' + '%02d'%team_two_seconds)

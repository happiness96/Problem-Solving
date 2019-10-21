#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

while True:
    start, duration = map(str, r().split())
    
    if start == duration == '00:00':
        break
    
    start_hour, start_min = map(int, start.split(':'))
    duration_hour, duration_min = map(int, duration.split(':'))
    
    end_hour = start_hour + duration_hour
    end_min = start_min + duration_min
    
    if end_min > 59:
        end_hour += 1
        end_min -=60
    
    ex_day = end_hour // 24
    end_hour %= 24
    
    print('%02d:%02d' % (end_hour, end_min), end='')
    
    if ex_day:
        print(' +%d' % ex_day, end='')
    
    print()

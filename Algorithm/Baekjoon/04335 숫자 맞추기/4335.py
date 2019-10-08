#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

your_name = 'Stan'              # 당신의 이름을 입력하세요

def say_number():
    return int(r())

def game_over():                
    exit()

def Is_it_right():
    return r().rstrip()

def Are_you_honest(correct_answer, game_set):
    for higher_number in game_set['high']:
        if higher_number <= correct_answer:
            print(your_name, 'is dishonest')
            return 0
        
    for lower_number in game_set['low']:
        if lower_number >= correct_answer:
            print(your_name, 'is dishonest')
            return 0
        
    print(your_name, 'may be honest')
    
def reset():
    return {'high':[], 'low':[]}

# Game Start
if __name__ == '__main__':
    game_set = {'high':[], 'low':[]}
    
    while 1:
        number = say_number()               # 상대방은 숫자를 말하게 됩니다.
        
        if number == 0:                     # 0을 말하게 된다면 게임은 종료됩니다.
            game_over()
        
        your_answer = Is_it_right()         # 숫자가 맞나요? 당신의 대답은?
        
        if your_answer == 'too high':       # 당신이 생각한 숫자보다 높다면 'high' 패에 숫자를 입력합니다.
            game_set['high'].append(number)
            
        elif your_answer == 'too low':      # 당신이 생각한 숫자보다 낮다면 'low' 패에 숫자를 입력합니다.
            game_set['low'].append(number)
        
        elif your_answer == 'right on':     # 당신이 생각한 숫자를 말했다면
            Are_you_honest(number, game_set)        # 당신이 여태까지 한 대답 중 거짓말을 한 게 있는지 체크하게 됩니다.
            game_set = reset()              # 이번 라운드는 종료되었습니다. 게임 패가 리셋됩니다.

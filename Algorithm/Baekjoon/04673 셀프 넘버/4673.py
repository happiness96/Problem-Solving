#-*- encoding: utf-8 -*-

not_self_numbers = {}           # 생성자가 있는 숫자들

for i in range(1,10001):
    ctor_numbers = i            # 생성자 초기값
    
    for c in str(i):            # 각 자리수를 합한다
        ctor_numbers += int(c)
    
    not_self_numbers[ctor_numbers] = 0    # 생성자가 있는 숫자를 저장

for i in range(1, 10001):
    if not i in not_self_numbers:       # 생성자가 아닌 숫자들을 제외하고 출력
        print(i)

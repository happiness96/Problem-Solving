#-*- encoding: utf-8 -*-
N = int(input())

def insert_next(num, num_list):     # DFS 방식
    num_list += str(num)
    
    if len(num_list) != N:      # 다 삽입한 것이 아니라면
        for i in range(1, N+1):
            if not str(i) in num_list:
                insert_next(i, num_list)
    else:
        for c in num_list:
            print(c, end=' ')
        print()
    
for i in range(1, N+1):
    insert_next(i,'')

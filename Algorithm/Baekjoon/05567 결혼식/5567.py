#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

n = int(r())        # 상근이의 동기의 수
m = int(r())        # 친구 관계 리스트의 길이

friend_connect = {}     # 친구 관계
my_friends = []          # 상근이의 친구들

for i in range(1, n + 1):
    friend_connect[i] = []
    
for i in range(m):
    a, b = map(int,r().split())     # 친구 관계인 둘
    
    if a == 1:      # 내 친구일 경우
        my_friends.append(b)
        continue
    
    if b == 1:
        my_friends.append(a)
        continue
    
    friend_connect[a].append(b)
    friend_connect[b].append(a)

friend_friend = []          # 친구의 친구

for my_friend in my_friends:        # 친구의 친구들 찾기
    for fr_fr in friend_connect[my_friend]:
        if not fr_fr in friend_friend and not fr_fr in my_friends:
            friend_friend.append(fr_fr)


print(len(my_friends) + len(friend_friend))

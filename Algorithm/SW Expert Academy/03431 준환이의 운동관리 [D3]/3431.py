#-*- encoding: utf-8 -*-
 
T = int(input())        # T: 테스트 케이스의 개수
 
for i in range(T):
    # 일주일에 L분 이상 U분 이하의 운동을 해야한다.
    # 준환이는 이번주에 X분만큼 운동을 했다. 
    L, U, X = map(int, input().split())
    print('#' + str(i+1), end=' ')
    print(-1 if X > U else max(0, L - X))

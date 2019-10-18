#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

k = int(r())        # k: 참가한 사람의 수
n = int(r())        # n: 전체 가로 줄의 수

final = r().rstrip()    # final: 사다리를 타고 난 후 결정된 최종 순서

pre = {}            # 감추어진 줄 이전
aft = {}            # 감추어진 줄 이후

ladder = []

for i in range(k):              # 참가한 사람의 수만큼 사다리에 입력
    ladder.append(chr(65 + i))


hidden_line = 0

for i in range(n):      # 감추어진 줄 찾기
    line = r().rstrip()
    
    if '?' in line:
        hidden_line = i
        break
    
    pre[i] = line


for i in range(n - hidden_line - 1):
    aft[i] = r().rstrip()


pre_ladder = {}        # 숨겨진 줄 앞까지 실행한 상태

for i in range(k):
    ind = i
    for j in range(hidden_line):
        chk = 0         # 1: 왼쪽, 2: 오른쪽
        if ind > 0:     # 사다리의 왼쪽에 막대가 있는지 체크
            if pre[j][ind-1] == '-':
                chk = 1
        
        if ind < k-1:   # 사다리의 오른쪽에 막대가 있는지 체크
            if pre[j][ind] == '-':
                chk = 2
        
        if chk == 1: ind -= 1
        elif chk == 2: ind += 1

    pre_ladder[ladder[i]] = ind


aft_ladder = {}

for i in range(k):
    ind = i
    for j in range(n - hidden_line - 1):      # 뒤에서부터 체크
        chk = 0         # 1: 왼쪽, 2: 오른쪽
        if ind > 0:     # 사다리의 왼쪽에 막대가 있는지 체크
            if aft[n-hidden_line-j-2][ind-1] == '-':
                chk = 1
        
        if ind < k-1:   # 사다리의 오른쪽에 막대가 있는지 체크
            if aft[n-hidden_line-j-2][ind] == '-':
                chk = 2
        
        if chk == 1: ind -= 1
        elif chk == 2: ind += 1
    
    aft_ladder[final[i]] = ind


hidden_ladder = ['*'] * (k-1)        # 숨겨진 사다리

for c in pre_ladder:
    if abs(pre_ladder[c] - aft_ladder[c]) > 1:    # 숨겨진 사다리를 만들 수 없는 경우
        print('x' * (k-1))
        exit()
        
    if pre_ladder[c] == aft_ladder[c] + 1:
        hidden_ladder[aft_ladder[c]] = '-'
        
    if pre_ladder[c] == aft_ladder[c] - 1:
        hidden_ladder[pre_ladder[c]] = '-'

# 검산
for c in pre_ladder:
    if pre_ladder[c] > 0:
        if hidden_ladder[pre_ladder[c]-1] == '-':
            if pre_ladder[c] - 1 != aft_ladder[c]:
                print('x' * (k-1))
                exit()
    
    if pre_ladder[c] < k-1:
        if hidden_ladder[pre_ladder[c]] == '-':
            if pre_ladder[c] + 1 != aft_ladder[c]:
                print('x' * (k-1))
                exit()


result = ''.join(hidden_ladder)

if '--' in result:            # 숨겨진 사다리를 만들 수 없는 경우
    print('x' * (k-1))
    exit()
    
print(result)

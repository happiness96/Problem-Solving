# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

RSP = list(r_input().rstrip().split())      # 가위 바위 보

# 양손 모두 동일한 것을 내는지 체크
ms = RSP[0] + RSP[1]
tk = RSP[2] + RSP[3]

if ms == 'RR' and 'P' in tk or ms == 'SS' and 'R' in tk or ms == 'PP' and 'S' in tk:          # 무조건 태경이가 이긴다면
    print('TK')

elif tk == 'RR' and 'P' in ms or tk == 'SS' and 'R' in ms or tk == 'PP' and 'S' in ms:            # 무조건 민성이가 이긴다면
    print('MS')

else:                                   # 승부를 예측할 수 없다면
    print('?')

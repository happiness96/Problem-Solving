# -*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

score = list(map(int, r().split()))     # 학생 50명의 점수

hong = int(r())             # 홍익이의 점수

rank = score.index(hong) + 1        # 홍익이의 등수

print('A+' if 1 <= rank <= 5 else 'A0' if rank <= 15 else 'B+' if rank <= 30 else 'B0' if rank <= 35 else 'C+' if rank <= 45 else 'C0' if rank <= 48 else 'F')

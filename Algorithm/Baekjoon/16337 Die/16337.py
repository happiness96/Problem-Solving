#-*- encoding: utf-8 -*-
import sys
r=sys.stdin.readline

die = []        # 주사위

for i in range(3):
    die.append(r().rstrip())

die_str = ''.join(die)
if die_str == 'o:o:o:o:o':
    print(5)

elif die_str == '::::o::::':
    print(1)

elif die_str in ['o:::o:::o', '::o:o:o::', ':::ooo:::', ':o::o::o:']:
    print(3)

elif die_str in ['ooo:::ooo', 'o:oo:oo:o']:
    print(6)

elif die_str == 'o:o:::o:o':
    print(4)

elif die_str in ['o:::::::o', '::o:::o::', ':o:::::o:', ':::o:o:::']:
    print(2)

else:
    print('unknown')

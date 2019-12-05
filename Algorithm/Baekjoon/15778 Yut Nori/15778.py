import sys
r_input = sys.stdin.readline

N = int(r_input())          # 윷을 던지고 말을 움직인 횟수

# 4 라인: 1 ~ 20
# 3 라인: 5, 31 ~ 32, 50, 34 ~ 35
# 2 라인: 10, 41 ~ 42, 50 ~ 52, 20
# 1 라인: 5, 31 ~ 32, 50 ~ 52, 20

location = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0}


def catch(my, aft):         # my: 현재 말, aft: 이동 후 위치, 상대 말을 잡는 지 검사하는 함수
    if my in 'abcd':
        for h in 'ABCD':
            if location[h] == aft:
                location[h] = 0

    else:
        for h in 'abcd':
            if location[h] == aft:
                location[h] = 0


def move(my, pre, aft):     # my: 현재 말, pre: 이동 전 위치, aft: 이동 후 위치, 현재 위치의 같은 편 말들을 이동
    if my in 'abcd':
        for h in 'abcd':
            if location[h] == pre:
                location[h] = aft

    else:
        for h in 'ABCD':
            if location[h] == pre:
                location[h] = aft


for _ in range(N):
    # horse가 던져서 나온 yut
    horse, yut = map(str, r_input().rstrip().split())

    go = yut.count('F')         # 1: 도, 2: 개, 3: 걸, 4: 윷

    if go == 0:
        go = 5          # 5: 모

    loc = location[horse]           # 말의 현재 위치

    if loc == 0:
        catch(horse, go)
        location[horse] = go

    elif loc == 5 or 31 <= loc <= 35:     # 3라인
        tmp = 30 + go if loc == 5 else loc + go          # 말의 이동 후 위치

        if tmp == 33:
            tmp = 50

        elif tmp > 35:
            tmp -= 21

        catch(horse, tmp)
        move(horse, loc, tmp)

    elif loc == 10 or 41 <= loc <= 42:      # 2라인
        tmp = 40 + go if loc == 10 else loc + go

        if tmp == 47:
            move(horse, loc, -1)

        else:
            if tmp == 46:
                tmp = 20

            elif tmp > 42:
                tmp += 7

            catch(horse, tmp)
            move(horse, loc, tmp)

    elif loc >= 50:                 # 1라인
        tmp = loc + go

        if tmp > 53:
            move(horse, loc, -1)

        else:
            if tmp == 53:
                tmp = 20

            catch(horse, tmp)
            move(horse, loc, tmp)

    else:
        tmp = loc + go

        catch(horse, tmp)
        move(horse, loc, tmp)
        

# 여기서부터 출력 부분
def print_board(s_horse, s_loc):
    print(s_horse[0] if location[s_horse[0]] == s_loc else s_horse[1] if location[s_horse[1]] == s_loc else '.', end='')


for i in range(10, 5, -1):
    print_board('Aa', i)
    print_board('Bb', i)
    print('----', end='')

print_board('Aa', 5)
print_board('Bb', 5)

print()

for i in range(10, 5, -1):
    print_board('Cc', i)
    print_board('Dd', i)
    print('    ', end='')

print_board('Cc', 5)
print_board('Dd', 5)

print()

print('| \\                          / |')
print('|  \\                        /  |')
print('|   \\                      /   |')

print('|    ', end='')
print_board('Aa', 41)
print_board('Bb', 41)
print('                  ', end='')
print_board('Aa', 31)
print_board('Bb', 31)
print('    |')

print_board('Aa', 11)
print_board('Bb', 11)
print('   ', end='')
print_board('Cc', 41)
print_board('Dd', 41)
print('                  ', end='')
print_board('Cc', 31)
print_board('Dd', 31)
print('   ', end='')
print_board('Aa', 4)
print_board('Bb', 4)

print()

print_board('Cc', 11)
print_board('Dd', 11)
print('     \\                /     ', end='')
print_board('Cc', 4)
print_board('Dd', 4)

print()

print('|       \\              /       |')
print('|        \\            /        |')

print('|         ', end='')
print_board('Aa', 42)
print_board('Bb', 42)
print('        ', end='')
print_board('Aa', 32)
print_board('Bb', 32)
print('         |')

print('|         ', end='')
print_board('Cc', 42)
print_board('Dd', 42)
print('        ', end='')
print_board('Cc', 32)
print_board('Dd', 32)
print('         |')

print_board('Aa', 12)
print_board('Bb', 12)
print('          \\      /          ', end='')
print_board('Aa', 3)
print_board('Bb', 3)

print()

print_board('Cc', 12)
print_board('Dd', 12)
print('           \\    /           ', end='')
print_board('Cc', 3)
print_board('Dd', 3)

print()

print('|             \\  /             |')

print('|              ', end='')
print_board('Aa', 50)
print_board('Bb', 50)
print('              |')

print('|              ', end='')
print_board('Cc', 50)
print_board('Dd', 50)
print('              |')

print('|             /  \\             |')

print_board('Aa', 13)
print_board('Bb', 13)
print('           /    \\           ', end='')
print_board('Aa', 2)
print_board('Bb', 2)

print()

print_board('Cc', 13)
print_board('Dd', 13)
print('          /      \\          ', end='')
print_board('Cc', 2)
print_board('Dd', 2)

print()

print('|         ', end='')
print_board('Aa', 34)
print_board('Bb', 34)
print('        ', end='')
print_board('Aa', 51)
print_board('Bb', 51)
print('         |')

print('|         ', end='')
print_board('Cc', 34)
print_board('Dd', 34)
print('        ', end='')
print_board('Cc', 51)
print_board('Dd', 51)
print('         |')

print('|        /            \\        |')
print('|       /              \\       |')

print_board('Aa', 14)
print_board('Bb', 14)
print('     /                \\     ', end='')
print_board('Aa', 1)
print_board('Bb', 1)

print()

print_board('Cc', 14)
print_board('Dd', 14)
print('   ', end='')
print_board('Aa', 35)
print_board('Bb', 35)
print('                  ', end='')
print_board('Aa', 52)
print_board('Bb', 52)
print('   ', end='')
print_board('Cc', 1)
print_board('Dd', 1)

print()

print('|    ', end='')
print_board('Cc', 35)
print_board('Dd', 35)
print('                  ', end='')
print_board('Cc', 52)
print_board('Dd', 52)
print('    |')

print('|   /                      \\   |')
print('|  /                        \\  |')
print('| /                          \\ |')

for i in range(15, 20):
    print_board('Aa', i)
    print_board('Bb', i)
    print('    ', end='')

print_board('Aa', 20)
print_board('Bb', 20)

print()

for i in range(15, 20):
    print_board('Cc', i)
    print_board('Dd', i)
    print('----', end='')

print_board('Cc', 20)
print_board('Cc', 20)

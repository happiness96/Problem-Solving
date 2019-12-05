import sys
r_input = sys.stdin.readline

N = int(r_input())          # 파일의 개수

files = list(map(int, r_input().split()))       # 각 파일들의 크기
cluster = int(r_input())            # 클러스터의 크기

total = 0

for f in files:
    if f:
        total += cluster * (f // cluster)

        if f % cluster:
            total += cluster

print(total)

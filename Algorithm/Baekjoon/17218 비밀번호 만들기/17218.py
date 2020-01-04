# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

string1 = r_input().rstrip()
string2 = r_input().rstrip()


def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    lcs_dp = [[0] * (len1 + 1) for _ in range(len2 + 1)]

    for i, ch1 in enumerate(str2):
        for j, ch2 in enumerate(str1):
            if ch1 == ch2:
                lcs_dp[i + 1][j + 1] = lcs_dp[i][j] + 1
            else:
                lcs_dp[i + 1][j + 1] = max(lcs_dp[i + 1][j], lcs_dp[i][j + 1])

    result = ''
    cnt = lcs_dp[-1][-1]

    row = len2
    col = len1

    while cnt:
        while True:
            if lcs_dp[row][col] != lcs_dp[row][col - 1]:
                break
            col -= 1

        while True:
            if lcs_dp[row][col] != lcs_dp[row - 1][col]:
                break
            row -= 1

        result += str1[col - 1]
        cnt -= 1

        row -= 1
        col -= 1

    return result[::-1]


print(lcs(string1, string2))

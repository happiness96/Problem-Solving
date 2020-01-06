# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline


def lcs(str1, str2, str3):
    lcs_dp = [[[0] * (len(str1) + 1) for _ in range(len(str2) + 1)] for _ in range(len(str3) + 1)]

    for i, ch1 in enumerate(str3):
        for j, ch2 in enumerate(str2):
            for k, ch3 in enumerate(str1):
                if ch1 == ch2 == ch3:
                    lcs_dp[i + 1][j + 1][k + 1] = lcs_dp[i][j][k] + 1
                else:
                    lcs_dp[i + 1][j + 1][k + 1] = max(lcs_dp[i + 1][j + 1][k], lcs_dp[i + 1][j][k + 1], lcs_dp[i][j + 1][k + 1])

    print(lcs_dp[-1][-1][-1])


string1 = r_input().rstrip()
string2 = r_input().rstrip()
string3 = r_input().rstrip()

lcs(string1, string2, string3)

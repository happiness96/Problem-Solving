# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

string1 = r_input().rstrip()
string2 = r_input().rstrip()


def lcs(str1, str2):
    len_s2 = len(str2)

    lcs_dp = [0] * (len_s2 + 1)

    for i, ch1 in enumerate(str1):
        tmp_dp = [0] * (len_s2 + 1)
        for j, ch2 in enumerate(str2):
            if ch1 == ch2:
                tmp_dp[j + 1] = lcs_dp[j] + 1
            else:
                tmp_dp[j + 1] = max(lcs_dp[j + 1], tmp_dp[j])
        lcs_dp = tmp_dp

    return lcs_dp[-1]


print(lcs(string1, string2))

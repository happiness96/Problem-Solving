# -*- encoding: utf-8 -*-
import sys
r_input = sys.stdin.readline

# 첫 번째 문자열과 두 번째 문자열을 입력받는다
string1 = r_input().rstrip()
string2 = r_input().rstrip()


def lcs(str1, str2):
    len_s1 = len(str1)
    len_s2 = len(str2)

    # LCS DP Table 생성
    lcs_dp = [[0] * (len_s1 + 1) for _ in range(len_s2 + 1)]

    for i in range(len_s2):
        for j in range(len_s1):
            if str2[i] == str1[j]:        # 두 개의 문자가 동일한 경우
                lcs_dp[i + 1][j + 1] = lcs_dp[i][j] + 1
            else:                   # 두 개의 문자가 다를 경우
                lcs_dp[i + 1][j + 1] = max(lcs_dp[i][j + 1], lcs_dp[i + 1][j])

    return lcs_dp[-1][-1]


print(lcs(string1, string2))

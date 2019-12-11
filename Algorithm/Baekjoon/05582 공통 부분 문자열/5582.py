# -*- encoding: utf-8 -*-
import sys

r_input = sys.stdin.readline

# 첫 번째 문자열과 두 번째 문자열을 입력받는다
string1 = r_input().rstrip()
string2 = r_input().rstrip()


def lcs(str1, str2):
    len_s1 = len(str1)

    # LCS DP Table 생성
    lcs_dp = [0] * (len_s1 + 1)
    maximum = 0

    for i, ch2 in enumerate(str2):
        tmp_dp = [0] * (len_s1 + 1)
        for j, ch1 in enumerate(str1):
            if ch2 == ch1:  # 두 개의 문자가 동일한 경우
                tmp = lcs_dp[j] + 1
                tmp_dp[j + 1] = tmp
                if tmp > maximum:
                    maximum = tmp
            else:  # 두 개의 문자가 다를 경우
                tmp_dp[j + 1] = 0

        lcs_dp = tmp_dp

    return maximum


print(lcs(string1, string2))

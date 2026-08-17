def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    # dp[i][j] = LCS length of text1[:i] and text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1   # chars match, extend the LCS
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])   # skip one char from either string

    return dp[m][n]


print(longest_common_subsequence("abcde", "ace"))   # 3
print(longest_common_subsequence("abc", "abc"))      # 3
print(longest_common_subsequence("abc", "def"))      # 0

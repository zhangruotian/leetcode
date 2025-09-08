class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j] = True if (dp[i][j-1] and s3[i+j-1]==s2[j-1]) or (dp[i-1][j] and s3[i+j-1]==s1[i-1])
        s1_len,s2_len,s3_len = len(s1),len(s2),len(s3)
        if s1_len+s2_len!=s3_len:
            return False
        dp = [[False]*(s2_len+1) for _ in range(s1_len+1)]
        dp[0][0]=True
        for i in range(1,s1_len+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1,s2_len+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1,s1_len+1):
            for j in range(1,s2_len+1):
                dp[i][j] = (dp[i][j-1] and s3[i+j-1]==s2[j-1]) or (dp[i-1][j] and s3[i+j-1]==s1[i-1])

        return dp[-1][-1]
# https://www.youtube.com/watch?v=rNC9u7nuf8c

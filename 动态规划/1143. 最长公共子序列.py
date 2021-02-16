class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # if text1[i]==text2[j]:
        #   dp[i][j]=dp[i-1][j-1]+1
        # else:
        #   dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        n1,n2=len(text1),len(text2)
        dp=[[0]*(n1+1) for _ in range(n2+1)]
        for i in range(n1):
            for j in range(n2):
                if text1[i]==text2[j]:
                    dp[j+1][i+1]=dp[j][i]+1
                else:
                    dp[j+1][i+1]=max(dp[j][i+1],dp[j+1][i])
        return dp[n2][n1]
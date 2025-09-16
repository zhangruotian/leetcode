class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # ab
        # ab
        # if s[i]==p[j]: dp[i][j]=dp[i-1][j-1]

        # ab
        # a. 
        # if p[j]=='.': dp[i][j]=dp[i-1][j-1]

        # 当p[j]=='*'并且p[j-1]!=s[i] and p[j-1]!='.'的时候：
        # ab
        # abc*
        # 此时dp[1][2]==False，说明确实需要dp
        # 0个c的情况下
        # if p[j]=='*': dp[i][j]=dp[i][j-2]

        # 当p[j]=='*'并且p[j-1]==s[i]或者p[j-1]=='.'的时候：（两种情况）
        # abccc
        # abc*
        # 1个或多个c的情况下
        # if p[j]=='*' and s[i]==p[j-1]: dp[i][j] = dp[i-1]dp[j] 
        # abc
        # abcc*
        # 0个c的情况下
        # dp[i][j]=dp[i][j-2]
        # 因此为dp[i][j] = dp[i-1][j] or dp[i][j-2]
        m,n = len(s),len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1,n+1):
            if p[j-1]=='*':
                dp[0][j]=dp[0][j-2]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==p[j-1]: 
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='.': 
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    if p[j-2]!=s[i-1] and p[j-2]!='.':
                        dp[i][j]=dp[i][j-2]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
        return dp[-1][-1]



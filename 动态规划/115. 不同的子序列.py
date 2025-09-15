class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j]: 到s[i]为止，能拼成到t[j]为止的subsequences的个数
        # ababa ba
        # if s[i]==t[j]: 
        # dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        # ababe ba
        # if s[i]!=t[j]: 
        # dp[i][j] = dp[i-1][j]
        m,n = len(s),len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

# DP题步骤：
# 1. 确定dp[i]或者dp[i][j]的意义
# 2. 推导转移方程dp[i]或者dp[i][j]可由前面已经解决的问题算出
# 3. 开始准备填表，思考如何初始化dp数组，能从小到大依次填表
# 4. 初始化
# 5. 填表。注意dp[i][j]中的i,j与s,t中s,j的mismatch

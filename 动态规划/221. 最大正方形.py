class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1 if matrix[i][j]=="1"
        #dp[i][j]=0 if matrix[i][j]=="0"
        #dp[i][j]表示以i，j为右下角的正方形的最大边长
        res=0
        h,w=len(matrix),len(matrix[0])
        dp=[[0]*(w+1) for _ in range(h+1)]
        for i in range(1,h+1):
            for j in range(1,w+1):
                if matrix[i-1][j-1]=="1":
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    res=max(res,dp[i][j])
                else:
                    dp[i][j]=0
        return res**2
#图片

#dp矩阵外层padding 0，使conner case的处理更简单。
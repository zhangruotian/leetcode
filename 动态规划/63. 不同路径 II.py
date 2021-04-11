class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[0]*(n+1) for _ in range(m+1)]
        if obstacleGrid[0][0]==1:
            return 0

        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==1 and j==1:
                    dp[i][j]=1
                else:
                    if obstacleGrid[i-1][j-1]==1:
                        dp[i][j]=0
                    else:
                        dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

#有障碍物的位置i,j，把dp[i][j]置为0即可。
#因为障碍物可能出现在第一行或第一列，因此不能像62题一样把第一行和第一列初始化为1
#应该padding 一层0，依次计算。当obstacleGrid[0][0]==1时，return0
# 其他情况把dp[1][1]初始化为1，依次计算即可

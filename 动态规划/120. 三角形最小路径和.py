class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==1:return triangle[0][0]
        self.res=float(inf)
        path=[triangle[0][0]]
        self.dfs(path,triangle,1,0)
        return self.res
    
    def dfs(self,path,triangle,level,index):
        if level>=len(triangle):return 
        for i in (index,index+1):
            path.append(triangle[level][i])
            if len(path)==len(triangle) and sum(path)<self.res:
                self.res=sum(path)
            self.dfs(path,triangle,level+1,i)
            path.pop()
# 回溯超时
# 本题不需要列举最小路径path，只要给出最小路径和。考虑dp

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
        n=len(triangle)
        dp=[[0]*i for i in range(1,n+1)]
        dp[0][0]=triangle[0][0]
        for i in range(1,n):
            for j in range(len(triangle[i])):
                if j==0:
                    dp[i][j]=dp[i-1][j]+triangle[i][j]
                elif j==len(triangle[i])-1:
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
        return min(dp[-1])
# S:O(n^2)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
        n=len(triangle)
        dp=[[0]*n for _ in range(2)]
        dp[0][0]=triangle[0][0]
        for i in range(1,n):
            for j in range(len(triangle[i])):
                if j==0:
                    dp[1][j]=dp[0][j]+triangle[i][j]
                elif j==len(triangle[i])-1:
                    dp[1][j]=dp[0][j-1]+triangle[i][j]
                else:
                    dp[1][j]=min(dp[0][j-1],dp[0][j])+triangle[i][j]
            dp[0],dp[1]=dp[1],dp[0]
        return min(dp[0])
## S:O(2n)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=triangle[-1][:]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(0,len(triangle[i])):
                dp[j]=min(dp[j],dp[j+1])+triangle[i][j]
        return dp[0]
# 最优解 S:O(n)
# 120.png 笔记
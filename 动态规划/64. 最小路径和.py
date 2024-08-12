class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i-1<0 and j-1<0:
                    dp[i][j] = grid[i][j]
                if i-1<0 and j-1>=0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                if i-1>=0 and j-1<0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                if i-1>=0 and j-1>=0:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]

#扩展： 返回路径
#在dp基础上记录路径，然后从最后一个往回找
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        path = [[0]*n for _ in range(m)]
        # 1 from top -1 from left
        for i in range(m):
            for j in range(n):
                if i-1<0 and j-1<0:
                    dp[i][j] = grid[i][j]
                if i-1<0 and j-1>=0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                    path[i][j] = -1
                if i-1>=0 and j-1<0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                    path[i][j] = 1
                if i-1>=0 and j-1>=0:
                    if dp[i-1][j]<=dp[i][j-1]:
                        path[i][j] = 1
                    else:
                        path[i][j] = -1
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        p,q = m-1,n-1
        trace = []
        while p>0 or q>0:
            trace.append(grid[p][q])
            direction = path[p][q] 
            if direction==1:
                p-=1
            if direction==-1:
                q-=1
        trace.append(grid[0][0])
        trace.reverse()
        print(trace)
        return sum(trace)

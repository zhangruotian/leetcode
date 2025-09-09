class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dfs_res = [[0]*n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res,self.dfs(i,j,m,n,matrix,dfs_res))
        return res
    
    def dfs(self,i,j,m,n,matrix,dfs_res):
        if dfs_res[i][j]:
            return dfs_res[i][j]

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        max_len = 0
        for di,dj in directions:
            if 0<=i+di<m and 0<=j+dj<n and matrix[i+di][j+dj]>matrix[i][j]:
                max_len = max(max_len,self.dfs(i+di,j+dj,m,n,matrix,dfs_res))
        dfs_res[i][j] = max_len+1
        return dfs_res[i][j]

# i,j dfs时同时记下路径上其它位置的dfs结果，存到dfs_res里面。
# i,j dfs时如果某di,dj在dfs_res里面，直接读取结果。
# dfs() return 当前i,j位置的最长路径；不要使用类似levels的方法，在每个di,dj都return i,j位置的结果，这样只能记录下dfs_res[i,j]，是记忆化dfs失效。
# 不需要维护prev，到下个递归里面判断大小。在本层直接能拿到下一层matrix[di,dj]的值。

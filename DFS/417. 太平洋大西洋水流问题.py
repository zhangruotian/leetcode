class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        a = [[0]*n for _ in range(m)]
        p = [[0]*n for _ in range(m)]
        for j in range(n):
            self.dfs(heights,p,0,j,0,m,n)
        for i in range(m):
            self.dfs(heights,p,i,0,0,m,n)
        for j in range(n):
            self.dfs(heights,a,m-1,j,0,m,n)
        for i in range(m):
            self.dfs(heights,a,i,n-1,0,m,n)
        res = []
        for i in range(m):
            for j in range(n):
                if a[i][j] and p[i][j]:
                    res.append([i,j])
        return res
    
    def dfs(self,heights,v,i,j,h,m,n):
        if i<0 or i>=m or j<0 or j>=n:
            return
        if heights[i][j]<h or v[i][j]:
            return 
        v[i][j]=1
        h = heights[i][j]
        self.dfs(heights,v,i+1,j,h,m,n)
        self.dfs(heights,v,i-1,j,h,m,n)
        self.dfs(heights,v,i,j+1,h,m,n)
        self.dfs(heights,v,i,j-1,h,m,n)
# https://www.youtube.com/watch?v=zV3o4XVoU8M
# 沿着四个边往里面走，创建两个2d list，每个记录a和p分别能到的地方，最后算交集

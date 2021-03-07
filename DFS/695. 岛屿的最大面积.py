class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res=0
        self.area=0
        row,col=len(grid),len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    self.area=0
                    self.dfs(i,j,row,col,grid)
                    self.res=max(self.res,self.area)
        return self.res
    
    def dfs(self,i,j,row,col,grid):
        if i<0 or i>row-1 or j<0 or j>col-1 or grid[i][j]==0:
            return 
        self.area+=1
        grid[i][j]=0
        self.dfs(i+1,j,row,col,grid)
        self.dfs(i-1,j,row,col,grid)
        self.dfs(i,j+1,row,col,grid)
        self.dfs(i,j-1,row,col,grid)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h=len(grid)
        w=len(grid[0])
        res=0
        for x in range(h):
            for y in range(w):
                if grid[x][y]=='1':
                    res+=1
                    self.dfs(grid,x,y,h,w)
        return res

    def dfs(self,grid,x,y,h,w):
        if x<0 or x>=h or y<0 or y>=w or grid[x][y]=='0':
            return
        grid[x][y]='0'
        self.dfs(grid,x+1,y,h,w)
        self.dfs(grid,x-1,y,h,w)
        self.dfs(grid,x,y+1,h,w)
        self.dfs(grid,x,y-1,h,w)

# 题型：DFS，不回溯  T:O(mn)
# DFS题，记得写终止条件。 return 代表结束本层递归函数，在上层看来就是结束了一行 比如self.dfs(grid,x+1,y,h,w)， 可以接着运行下一行了
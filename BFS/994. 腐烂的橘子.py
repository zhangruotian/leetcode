from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        res = -1
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
        while q:
            for _ in range(len(q)):
                pop_i,pop_j = q.popleft()
                self.rotting(grid,q,pop_i,pop_j,m,n)
            res+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return 0 if res==-1 else res
    
    def rotting(self,grid,q,i,j,m,n):
        if i-1>=0 and grid[i-1][j]==1:
            grid[i-1][j]=2
            q.append((i-1,j))
        if i+1<m and grid[i+1][j]==1:
            grid[i+1][j]=2
            q.append((i+1,j))
        if j-1>=0 and grid[i][j-1]==1:
            grid[i][j-1]=2
            q.append((i,j-1))
        if j+1<n and grid[i][j+1]==1:
            grid[i][j+1]=2
            q.append((i,j+1))
# BFS，每次只看刚被传染的橘子。O(MN)

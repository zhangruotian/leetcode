from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m,n = len(grid),len(grid[0])
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    q.append((i,j))
                    visited[i][j]=1
        dist = 0
        while q:
            for _ in range(len(q)):
                pop_i,pop_j = q.popleft()
                grid[pop_i][pop_j] = dist
                self.extend(grid,pop_i,pop_j,m,n,q,visited)
            dist+=1
    
    def extend(self,grid,i,j,m,n,q,visited):
        if i-1>=0 and grid[i-1][j]!=-1 and grid[i-1][j]!=0 and not visited[i-1][j]:
            q.append((i-1,j))
            visited[i-1][j]=1
        if i+1<m and grid[i+1][j]!=-1 and grid[i+1][j]!=0 and not visited[i+1][j]:
            q.append((i+1,j))
            visited[i+1][j]=1
        if j-1>=0 and grid[i][j-1]!=-1 and grid[i][j-1]!=0 and not visited[i][j-1]:
            q.append((i,j-1))
            visited[i][j-1]=1
        if j+1<n and grid[i][j+1]!=-1 and grid[i][j+1]!=0 and not visited[i][j+1]:
            q.append((i,j+1))
            visited[i][j+1]=1
      #类似994腐烂的茄子，多源bfs，逐渐扩散

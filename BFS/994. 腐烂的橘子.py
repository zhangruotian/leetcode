from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
        res = -1
        while q:
            for _ in range(len(q)):
                popped_i,popped_j = q.popleft()
                directions = [(-1,0),(1,0),(0,-1),(0,1)]
                for di,dj in directions:
                    new_i,new_j = popped_i+di,popped_j+dj
                    if new_i<0 or new_i>=m or new_j<0 or new_j>=n:
                        continue
                    if grid[new_i][new_j]==0 or grid[new_i][new_j]==2:
                        continue
                    grid[new_i][new_j]=2
                    q.append((new_i,new_j))
            res+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return 0 if res==-1 else res
# BFS，每次只看刚被传染的橘子。O(MN)

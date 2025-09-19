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
# 沿着四个边往里面走，创建两个2d list，每个记录a和p分别能到的地方，最后算交集
# pa有两个作用。
# 1. 对于pacific的两个点p1,p2来说，只要p2走到了p1走过的地方，后面不用看了，跟p1后面走的位置一样，所以看到True直接return就行。
# 2. 对于某个点p1来说，pa还能防止回头，因为走过的为True，看到True直接return就行。
# Time: O(m,n)


from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        pa = [[False]*n for _ in range(m)]
        aa = [[False]*n for _ in range(m)]
        q = deque()
        res = []
        for i in range(m):
            q.append((i,0))
        for j in range(n):
            q.append((0,j))
        self.bfs(heights,q,pa,m,n)
        for i in range(m):
            q.append((i,n-1))
        for j in range(n):
            q.append((m-1,j))
        self.bfs(heights,q,aa,m,n)
        for i in range(m):
            for j in range(n):
                if aa[i][j] and pa[i][j]:
                    res.append([i,j])
        return res
    
    def bfs(self,heights,q,a,m,n):
        while q:
            i,j = q.popleft()
            if a[i][j]:
                continue
            a[i][j]=True
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for gi,gj in directions:
                if 0<=i+gi<m and 0<=j+gj<n and heights[i+gi][j+gj]>= heights[i][j] and not a[i+gi][j+gj]:
                    q.append((i+gi,j+gj))
        
# BFS. 同样的思想，注意要把所有pacific或者Atlantic都入队后，再BFS，减少多余操作。
# 因为是出队标记True，入队的时候可能有重复，记得跳过，减少多余操作。
# Time: O(m,n)

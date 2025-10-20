class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board),len(board[0])
        surrounded = []
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j]=='O':
                    path = []
                    if not self.dfs(board,visited,path,i,j,m,n):
                        surrounded.extend(path)
        for i,j in surrounded:
            board[i][j]='X'
                
    def dfs(self,board,visited,path,i,j,m,n):
        if i<0 or i>=m or j<0 or j>=n:
            return True
        if visited[i][j] or board[i][j]=='X':
            return False
        visited[i][j]=1
        path.append((i,j))
        t = self.dfs(board,visited,path,i+1,j,m,n)
        b = self.dfs(board,visited,path,i-1,j,m,n)
        r = self.dfs(board,visited,path,i,j+1,m,n)
        l = self.dfs(board,visited,path,i,j-1,m,n)
        if t or b or r or l:
            return True
        return False
# 遇到O开始搜索，搜索完所有的方向才能知道，这个岛屿应该mark成'X'还是'O'
# 在搜索的途中记录下path，如果是个被围绕的岛屿，最后改为'X'
# 走过的位置改为'V'，后面遇到同一个岛屿的不同位置，不进入dfs。
